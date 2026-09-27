# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with this repository.

## Repository Purpose

A Claude Code plugin marketplace for solo, non-technical, and bootstrapped founders building web apps with AI tools (Claude Code, Lovable, Replit, Cursor). It holds 10 public plugins plus one plugin for skill authors. The skills cover the full build lifecycle plus business, marketing, and growth strategy.

## Structure

One marketplace, many plugins. The marketplace manifest lives at `.claude-plugin/marketplace.json`. It lists every plugin with a relative `source` of `./plugins/<plugin>`.

### `plugins/<plugin>/` — One Plugin Each

- `.claude-plugin/plugin.json` — the plugin manifest, with its own `version`
- `skills/` — one subdirectory per skill, each with `SKILL.md` (required) plus optional supporting files
- `commands/` — custom commands (only `sf-core` has one: `improve-prompt.md`)

Run `ls plugins/*/skills/` for the current list. Read a skill's `description` frontmatter to see what it covers. `sf-dev` holds skill-authoring tools and stays out of the README.

### Adding or Moving a Skill

Each skill belongs to exactly one plugin. When you add, move, or rename a skill, update these three places so the routers stay correct:

- The plugin table at the end of `plugins/sf-core/skills/journey/SKILL.md`
- The same table in `plugins/sf-core/skills/next/SKILL.md`
- The plugin section under "What's Inside" in `README.md`

Bump the `version` in that plugin's `plugin.json` when you ship a change to it.

## File Conventions

- All files use ALL CAPS with hyphens: `DEBUG-PROMPTS.md`, not `debug_prompts.md`
- SKILL.md files use YAML frontmatter with `name` and `description` fields
- Skills are designed for progressive disclosure: SKILL.md first, then supporting files
- Never more than 1 level deep from SKILL.md
- In a SKILL.md body, write dollar amounts as `\$29/mo`, not `$29/mo`. Claude Code replaces `$0`, `$1`, and so on with the words the user typed after the skill name. The backslash stops this, and Claude Code removes it before the model reads the skill. Amounts followed by a letter (`$10k`, `$1M`) are safe without it.

## Design Philosophy

These skills assume Claude's intelligence — they focus on:
- Non-technical founder perspective and common mistakes
- Tool selection criteria (when to use Lovable vs Claude Code vs Replit)
- Actionable checklists and "Tell AI:" copy-paste prompts
- What's out of scope (preventing premature optimization)
- Concise, actionable content that avoids explaining concepts Claude already knows
