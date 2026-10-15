@AGENTS.md

# Claude Code specifics

## Overrides of global instructions (this repo only)

- Teaching mode: explanations, worked examples and "why" are expected. The global "be concise / don't explain basics" rule does not apply to teaching content. Stay concise in logistics.
- Lab graders (pytest) run whenever the learner asks to check work, not only before commits.
- Commits and pushes here are automatic; the global "ask before commit/push" rule does not apply to this repo.
- The code-review-graph instructions apply only when reading the learner's work code live (work boundary in `AGENTS.md`), never to this repo.

## Session trigger

"start" / "ready" invoke the `start` skill, which runs `protocol/session.md`.

## Hooks (`.claude/settings.json`)

- `Stop` (10-minute throttle) and `SessionEnd` run `scripts/autosave.sh`: commit and push.
- `UserPromptSubmit` runs `scripts/checkpoint_reminder.sh`. When a "CHECKPOINT DUE" reminder appears, checkpoint per `AGENTS.md` before replying.

## Subagents (`.claude/agents/`)

- `lab-reviewer`: design review of lab work per `protocol/lab-review.md`.
- `resource-scout`: finds current, high-quality references online.

Use parallel subagents for independent research or review; workflows only when the learner explicitly asks for multi-agent orchestration. Use `/loop` and background monitors for long-running jobs (e.g., Yocto builds).

## Git

For `glab` on gitlab.com, unset `GITLAB_TOKEN` first (it holds a different account's token).
