#!/usr/bin/env bash
# Response timer. "mark" records when a reply ends; "report" prints the learner's response time.
cd "$(dirname "$0")/.." || exit 0
stamp=.git/last-reply
case "${1:-}" in
    mark)
        date +%s > "$stamp"
        ;;
    report)
        [ -f "$stamp" ] || exit 0
        elapsed=$(( $(date +%s) - $(cat "$stamp") ))
        if [ "$elapsed" -lt 7200 ]; then
            printf '[timer] learner response time: %dm %02ds\n' $((elapsed / 60)) $((elapsed % 60))
        fi
        ;;
esac
exit 0
