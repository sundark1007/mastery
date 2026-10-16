# Session Protocol

Followed on "start", "ready", "let's go", "resume". Tool-neutral: where a step names a tool-specific capability, any assistant may perform the same step directly.

Hats per `AGENTS.md`: Friend to open, Tester for recall and the diagnostic, Teacher for concepts, Colleague for labs, Interviewer for explain-back and Friday synthesis, Guide to close.

## 1. Load state

Read `learner/profile.md`, `learner/review_queue.md`, `roadmap.md`, and the most recent file in `journal/`. If in Phase 0, also read `diagnostic/plan.md` and `diagnostic/progress.md`. Note today's date and weekday.

## 2. Open (3–4 lines max)

- Where we are (phase, module, last session's resume point).
- Today's plan in one line.
- One question: "Anything from work this week you want to tie in?" Discuss it live; fold only the generic concept into today's work (work boundary in `AGENTS.md`).

If the last session ended mid-task, resume exactly at the recorded point.

## 3. Recall (5–10 min)

Ask up to 4 due items from the review queue, one at a time, no hints. For each answer ask for confidence (1–5), then give the correct answer briefly. Update intervals per `AGENTS.md`.

## 4. Pick today's work

- Phase 0: continue the diagnostic from `diagnostic/progress.md` (exact next question or lab), per `diagnostic/plan.md`. On the very first diagnostic session, explain the format in four lines: adaptive, one question at a time, confidence 1–5 on every answer, "I don't know" is a good answer, `pause` saves everything.
- Otherwise: the next module in the roadmap, unless the profile shows a blocking gap (detour first) or the learner asked to change pace.
- Friday: synthesis session in interview mode (timed cross-domain problem, timed design discussion), then the weekly retro.

## 5. Concept (≈15 min)

1. Ask what the learner already thinks or would guess. Teach to the gap.
2. Build the mental model from first principles; show it through at least two domains.
3. `connect`: relate it to the learner's work code, live in conversation only, per the work boundary in `AGENTS.md`. Nothing from this step is written to any file.
4. Assign pre-reading from the external course library when a lesson matches.
5. Check facts that drift (versions, APIs, services) online before stating them.

## 6. Lab (≈25–30 min)

1. Create or open the lab under `labs/` or `fleet/`: README with spec and acceptance criteria, stub, pytest grader. The learner writes the implementation.
2. Support with the hint ladder only (nudge → question → concept pointer → partial sketch → solution on explicit request, logged as a gap).
3. On `check`: run the grader in WSL, then review the design per `protocol/lab-review.md` (in Claude Code, via the `lab-reviewer` subagent). Present findings as teaching points with the named principle and its why.

## 7. Explain-back (5–10 min)

Interview mode (timed, per `AGENTS.md`). The learner explains the concept as if teaching a colleague. Probe one edge case, one trade-off, one failure mode. Score against the mastery scale and note time against budget.

## 8. Close (always, even on `pause`)

1. Update `learner/profile.md`: levels (evidence only), strengths, gaps, misconceptions, calibration, session count, current position.
2. Add review items for every new concept and every miss.
3. Write `journal/YYYY-MM-DD.md` (work boundary applies): covered, evidence, AI capabilities used and why, which assistant ran the session, plan adjustments, exact resume point.
4. Adjust `roadmap.md` if evidence warrants it (record why in the journal).
5. Commit and push: `bash scripts/autosave.sh "session close"`.

## Pacing rules

- Two misses on the same idea → slow down: smaller step, new angle, check the prerequisite.
- Fast, correct, confident and able to transfer → offer to skip ahead.
- Watch the clock: at ~50 min move to Close, saving any unfinished lab as the resume point.
