# Learning Model

## Principles

1. **Understanding over performance.** The goal is to derive, explain and apply; tests and quizzes are evidence, not the target.
2. **Integration.** Every concept is learned through at least two domains and lands as a component of Fleet.
3. **Connected to real work, live only.** Concepts may be related to day-to-day work in conversation; nothing work-related is ever recorded in this repo (work boundary in `AGENTS.md`).
4. **Retrieval first.** Each concept starts with what the learner already thinks; teaching targets the gap.
5. **The learner writes the code.** Help comes as a hint ladder: nudge → question → concept pointer → partial sketch → full solution only on request (logged as a gap).
6. **Quality is part of correctness.** Lab work is reviewed for clarity, modularity, config-driven design, DRY, typing and testability, and each review names the principle involved.

## Baseline

Phase 0 is an adaptive diagnostic over every domain ([`diagnostic/plan.md`](../diagnostic/plan.md)): verbal questions at four levels, five hands-on labs and a written design exercise. Each answer carries a confidence rating, which separates real knowledge, lucky guesses and misconceptions.

## Mastery scale

| Level | Meaning |
|---|---|
| 0 | Unfamiliar |
| 1 | Recognizes terms |
| 2 | Explains the concept correctly |
| 3 | Applies it with guidance |
| 4 | Applies it independently in new contexts, handles edge cases |
| 5 | Teaches it, reasons about trade-offs and failure modes, derives it from first principles |

Levels change only on evidence: graded labs, unprompted explanations, transfer to new problems. Core concepts gate progression at level 4.

## Calibration

Confidence is compared with correctness. Over-confident misses are misconceptions and get top priority; under-confident hits show knowledge to build trust in.

## Spaced repetition

Every new concept and every miss becomes a review item. Intervals: 1, 3, 7, 14, 30, 60, 120 days. Correct and confident advances the interval, correct but unsure repeats it, and a miss resets it to one day. Reviews require recall or reasoning, never recognition.

## Adaptation

- Two misses on the same idea: slow down, change the angle, check prerequisites.
- Fast, correct, confident answers that transfer to new problems: skip ahead.
- Weekly retros tune pace and difficulty; monthly reviews re-order the roadmap and refresh resources; quarterly snapshots record the mastery map so progress is visible over time.

## AI as a skill

AI proficiency is a domain of its own and also the medium of learning. The tutor names each AI capability it uses (subagents, skills, hooks, web research, plan mode, loops, workflows) and why. Over time the learner builds their own tooling for this repo, then builds AI tools for real work.

## Records

| File | Holds |
|---|---|
| `learner/profile.md` | Mastery map, strengths, gaps, misconceptions, portfolio, snapshots |
| `learner/review_queue.md` | Review items and due dates |
| `journal/` | Per-session evidence, decisions, plan changes, resume point |
