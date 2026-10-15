@./AGENTS.md

# Gemini specifics

Read `AGENTS.md` (imported above) and follow it as your operating manual. On "start" or "ready", follow `protocol/session.md`.

- No hooks run under Gemini: checkpoint to the journal yourself roughly every 10 minutes, and always finish with `bash scripts/autosave.sh "session close"` so the work is committed and pushed.
- Lab design reviews: apply `protocol/lab-review.md` directly.
- Record "assistant: Gemini" in the journal entry for the session.
