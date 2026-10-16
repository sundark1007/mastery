# Engineering Mastery Program

A personal, open-ended program to build deep, all-round engineering mastery: understanding each concept well enough to explain it from first principles, implement it, and reason about its trade-offs and failure modes.

The AI tutor switches between friend, guide, teacher, colleague, tester and interviewer, whichever fits the moment. One hour a day, Monday to Friday, no end date. Say **start** and the tutor resumes exactly where the last session ended.

## What it covers

| Area | Domains |
|---|---|
| Software craft | Python, object-oriented design, clean code and design principles, testing and typing |
| Computer science | Data structures, algorithms |
| Systems | Operating systems, Linux internals, computer architecture, C and systems programming |
| Devices | Embedded systems, device interfaces and protocols, Yocto |
| Connected systems | Networking, IPC, MQTT and IoT, distributed systems |
| Architecture | System design, cloud architecture, databases |
| Cross-cutting | Security, debugging and performance, technical communication |
| Leverage | AI-assisted engineering |

Domains are taught together, never in isolation. A heap is learned as the timer queue of a scheduler, written in idiomatic Python, and reviewed against design principles. A ring buffer is learned as the receive path of a serial driver.

## The spine project: Greenhouse

Every phase adds real components to one system: a simulated greenhouse climate controller with sensor and actuator buses, protocol codecs, an event bus, a rules engine, a scheduler, a supervisor, a state store, a cloud bridge and a broker cluster. Later parts move to C and get packaged into a Yocto image. By the end, every concept exists as working, tested code in one coherent design. See [`roadmap.md`](roadmap.md).

## Quick start

1. Open a terminal in this folder and run `claude`.
2. Say **start**.

The first time, follow [`docs/setup.md`](docs/setup.md) to prepare the WSL lab environment.

## A session

| Block | Minutes | What happens |
|---|---|---|
| Recall | 5–10 | Due review items, answered from memory |
| Concept | 15 | Retrieval first, then teaching anchored to real code |
| Lab | 25–30 | You implement; graders and a design review check it |
| Explain-back | 5–10 | You teach it back; edge cases and trade-offs are probed |
| Close | 2 | Progress recorded, next step set, work committed |

Friday is synthesis: a cross-domain problem, a design discussion and a short weekly retro that can reshape the plan.

## Commands

| Say | Effect |
|---|---|
| `start` / `ready` | Begin or resume a session |
| `slow down` | More examples, smaller steps, prerequisite detour if needed |
| `go deeper` | Internals, edge cases, failure modes, primary sources |
| `skip` | Prove mastery with a quick check, then move on |
| `hint` | Next rung of the hint ladder |
| `explain differently` | New analogy or a different domain as the entry point |
| `check` | Run the lab grader and design review |
| `connect` | Relate the concept to your work code, live only; never recorded |
| `pause` | Save an exact resume point and stop |
| `where am I` | Current position, recent progress, what's next |
| `retro` | Review progress and adjust the plan |
| `interview mode` / `interview mode off` | Timed questions with budgets and time feedback |

## Repository layout

```text
AGENTS.md                 Tutor operating manual (any assistant)
CLAUDE.md, GEMINI.md      Tool-specific additions; both import AGENTS.md
protocol/
  session.md              Session protocol
  lab-review.md           Lab design review rubric
scripts/                  Autosave and checkpoint scripts
roadmap.md                Phases, modules and continuous threads (living)
learner/
  profile.md              Mastery map, strengths, gaps, misconceptions, portfolio
  review_queue.md         Spaced-repetition items and due dates
journal/                  One entry per session: evidence, decisions, resume point
diagnostic/plan.md        Baseline assessment protocol and question bank
labs/                     Hands-on exercises, each with a spec, stub and grader
greenhouse/               The spine project
docs/                     Setup and learning-model documentation
local/                    Machine-specific context, git-ignored, never committed
.claude/
  skills/start/           Claude Code entry point to protocol/session.md
  agents/                 lab-reviewer, resource-scout
  settings.json           Hook wiring
```

## Using other assistants

All state and protocol are plain markdown, so any coding assistant with file and shell access can resume a session: open a local clone, say **start**. `AGENTS.md` is the shared manual; `GEMINI.md` adapts it for Gemini CLI. Without Claude Code hooks, the assistant checkpoints and commits by following `AGENTS.md`. A read-only chat assistant can teach from the repo, but its session is not recorded.

## Progress is never lost

- Hooks commit and push to private GitHub and GitLab repos at most every 10 minutes after a reply and at session end.
- A checkpoint reminder makes the tutor record the session state when nothing has been written for 10 minutes.
- All progress lives in files, never in chat memory.

Details: [`docs/setup.md`](docs/setup.md#automation).

## Further reading

- [`docs/learning-model.md`](docs/learning-model.md) — how teaching, assessment and adaptation work.
- [`docs/setup.md`](docs/setup.md) — environment, editor, remotes and automation.
