#!/bin/bash
# Hook #3: Warn before deploying without running tests first
# PreToolUse hook for Bash commands that look like deployments

INPUT=$(cat)
CMD=$(echo "$INPUT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('tool_input',{}).get('command',''))" 2>/dev/null)

# Match common deploy commands
if echo "$CMD" | grep -qE '(vercel deploy|vercel --prod|netlify deploy|fly deploy|fly launch|railway up|render deploy|git push.*(main|master|production|deploy)|npm run deploy|npx wrangler deploy|amplify publish|firebase deploy|supabase functions deploy)'; then
  echo '{
    "hookSpecificOutput": {
      "hookEventName": "PreToolUse",
      "permissionDecision": "ask",
      "permissionDecisionReason": "Deploy command detected. Have you run tests? Consider using /test first."
    }
  }'
else
  exit 0
fi
