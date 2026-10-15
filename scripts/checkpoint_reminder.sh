#!/usr/bin/env bash
# Remind the tutor to checkpoint session state when nothing has been recorded for 10 minutes.
cd "$(dirname "$0")/.." || exit 0
[ -f .git/session-start ] || exit 0
latest=$(cat .git/session-start)
journal=$(ls -t journal/*.md 2>/dev/null | head -1)
if [ -n "$journal" ]; then
    mtime=$(date -r "$journal" +%s)
    [ "$mtime" -gt "$latest" ] && latest=$mtime
fi
if [ $(( $(date +%s) - latest )) -ge 600 ]; then
    echo "CHECKPOINT DUE: before responding, append to today's journal what was covered so far, evidence gathered, and the exact resume point; update learner/profile.md and learner/review_queue.md if anything changed."
fi
exit 0
