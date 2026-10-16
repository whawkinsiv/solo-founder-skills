#!/usr/bin/env python3
"""Check whether domains are registered. Two passes: DNS, then RDAP.

Usage:
    python3 check-availability.py foothold.dev traction.com getclay.io
    python3 check-availability.py --file candidates.txt
    python3 check-availability.py --json foothold.dev

Why two passes: DNS is instant and free but only proves a domain IS taken
(an NS record means somebody delegated it). Silence from DNS does not prove
a domain is free, because a registered domain can sit with no nameservers.
RDAP is the registry's own record, so it answers the real question.

Why the TLD check matters: not every TLD runs an RDAP server. As of this
writing .io, .co, .me and .sh do not. On those, RDAP returns 404 for every
domain, taken or not, so a 404 there is meaningless. The script reads IANA's
bootstrap file to learn which TLDs it can trust, and refuses to guess on the
rest.

No API key. No account. RDAP is the official successor to WHOIS.
"""

import argparse
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request

BOOTSTRAP_URL = "https://data.iana.org/rdap/dns.json"
RDAP_URL = "https://rdap.org/domain/{}"
TIMEOUT = 12
PAUSE = 1.1  # rdap.org rate-limits; stay under it

TAKEN = "TAKEN"
FREE = "LIKELY FREE"
UNVERIFIED = "UNVERIFIABLE"
ERROR = "ERROR"


def fetch_rdap_tlds():
    """Return the set of TLDs that have an RDAP server, or None if unreachable."""
    try:
        with urllib.request.urlopen(BOOTSTRAP_URL, timeout=TIMEOUT) as r:
            data = json.load(r)
    except (urllib.error.URLError, OSError, ValueError, TimeoutError):
        return None
    tlds = set()
    for service in data.get("services", []):
        if service:
            tlds.update(t.lower() for t in service[0])
    return tlds


def has_ns(domain):
    """True if the domain has nameservers. Proves it is registered."""
    for cmd in (["dig", "+short", "+time=4", "+tries=1", "NS", domain],
                ["host", "-t", "NS", domain]):
        try:
            out = subprocess.run(cmd, capture_output=True, text=True, timeout=12)
        except (FileNotFoundError, subprocess.TimeoutExpired):
            continue
        text = out.stdout.strip()
        if not text:
            return False
        if cmd[0] == "dig":
            return bool(text)
        return "name server" in text
    return None  # no resolver tool available


def rdap_status(domain):
    """Return an HTTP status code from RDAP, retrying once on a rate limit."""
    req = urllib.request.Request(
        RDAP_URL.format(domain),
        headers={"Accept": "application/rdap+json", "User-Agent": "solo-founder-skills/1.0"},
    )
    for attempt in (1, 2):
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                return r.status
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt == 1:
                time.sleep(5)
                continue
            return e.code
        except (urllib.error.URLError, OSError, TimeoutError):
            return None
    return None


def classify(domain, rdap_tlds):
    """Decide whether a domain is taken, free, or unanswerable."""
    tld = domain.rsplit(".", 1)[-1].lower()
    ns = has_ns(domain)

    if ns:
        return TAKEN, "has nameservers"

    covered = rdap_tlds is not None and tld in rdap_tlds
    if not covered:
        reason = (f".{tld} has no RDAP server, so registration cannot be confirmed here"
                  if rdap_tlds is not None else "IANA bootstrap unreachable")
        return UNVERIFIED, f"no nameservers, but {reason}"

    code = rdap_status(domain)
    time.sleep(PAUSE)

    if code == 404:
        return FREE, "no nameservers, RDAP has no record"
    if code == 200:
        return TAKEN, "RDAP has a registration record"
    if code == 429:
        return UNVERIFIED, "RDAP rate-limited; re-run this one in a minute"
    if code is None:
        return ERROR, "RDAP unreachable (network or DNS problem)"
    return UNVERIFIED, f"RDAP returned {code}"


def valid(domain):
    return bool(re.fullmatch(r"[a-z0-9]([a-z0-9-]*[a-z0-9])?(\.[a-z]{2,})+", domain))


def main():
    p = argparse.ArgumentParser(description="Check whether domains are registered.")
    p.add_argument("domains", nargs="*", help="e.g. foothold.dev traction.com")
    p.add_argument("--file", help="file with one domain per line")
    p.add_argument("--json", action="store_true", help="emit JSON instead of a table")
    args = p.parse_args()

    names = [d.strip().lower() for d in args.domains]
    if args.file:
        with open(args.file) as f:
            names += [ln.strip().lower() for ln in f if ln.strip() and not ln.startswith("#")]
    if not names:
        p.error("give at least one domain, or --file")

    rdap_tlds = fetch_rdap_tlds()
    if rdap_tlds is None:
        print("warning: could not reach IANA bootstrap; every TLD will read as "
              "UNVERIFIABLE\n", file=sys.stderr)

    results = []
    for d in names:
        if not valid(d):
            results.append({"domain": d, "status": ERROR, "reason": "not a valid domain name"})
            continue
        status, reason = classify(d, rdap_tlds)
        results.append({"domain": d, "status": status, "reason": reason})

    if args.json:
        print(json.dumps(results, indent=2))
        return

    width = max(len(r["domain"]) for r in results) + 2
    print(f"{'DOMAIN':<{width}}{'VERDICT':<14}WHY")
    print("-" * (width + 14 + 44))
    for r in results:
        print(f"{r['domain']:<{width}}{r['status']:<14}{r['reason']}")

    free = [r["domain"] for r in results if r["status"] == FREE]
    unv = [r["domain"] for r in results if r["status"] == UNVERIFIED]
    print()
    if free:
        print(f"Likely free ({len(free)}): {', '.join(free)}")
        print("  Confirm at a registrar before you commit. Only a registrar is final.")
    if unv:
        print(f"Needs a manual check ({len(unv)}): {', '.join(unv)}")
        print("  Search these at your registrar. This tool cannot answer them.")


if __name__ == "__main__":
    main()
