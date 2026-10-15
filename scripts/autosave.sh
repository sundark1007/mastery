#!/usr/bin/env bash
# Commit all program changes and push to the remotes. Usage: autosave.sh [--throttle SECONDS] [label]
cd "$(dirname "$0")/.." || exit 0
throttle=0
if [ "${1:-}" = "--throttle" ]; then throttle=$2; shift 2; fi
label=${1:-autosave}
stamp=.git/autosave-last
now=$(date +%s)
if [ "$throttle" -gt 0 ] && [ -f "$stamp" ] && [ $((now - $(cat "$stamp"))) -lt "$throttle" ]; then
    exit 0
fi
echo "$now" > "$stamp"
git add -A 2>/dev/null
if ! git diff --cached --quiet; then
    if ! out=$(git commit -q -m "$label $(date '+%Y-%m-%d %H:%M')" 2>&1); then
        echo "Autosave commit blocked; fix the content, never bypass the guard:" >&2
        echo "$out" >&2
        exit 2
    fi
fi
timeout 30 git push -q origin HEAD >/dev/null 2>&1
exit 0
