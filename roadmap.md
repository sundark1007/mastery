# Roadmap

A living plan. Phases set direction, not deadlines; order and depth adapt to evidence in `learner/profile.md`. Changes are recorded in the journal.

## Spine project: Greenhouse

A simulated greenhouse climate controller built in Python (later partly in C and packaged with Yocto). Every phase adds real components, so each concept ends up as working, tested code inside one coherent system. All design comes from first principles and public references; see the work boundary in `AGENTS.md`.

```text
 simulated devices ──► bus/protocol layer ──► event bus ──► rules/FSM engine
        (radio, serial)   (codec, CRC)          (IPC)          (rules)
                                                  │
                    scheduler ── supervisor ── state store ── cloud bridge ──► mini broker / cluster
                    (OS sim)     (restarts)     (cache)        (MQTT)           (distributed)
```

## Domain codes

PY Python · OO OOP & design · EP engineering practice (testing, typing, clean code) · DS data structures · AL algorithms · OS operating systems · LX Linux internals · CA computer architecture · EM embedded & devices · YO Yocto & builds · NW networking · DI distributed systems · SD system design · CL cloud architecture · IO IPC, MQTT & IoT · AI AI-assisted engineering

## Phase 0 — Baseline

- Adaptive diagnostic across all domains (`diagnostic/plan.md`): verbal rounds, hands-on labs and a design exercise.
- Lab environment in WSL; learning protocol tuned to the learner.
- Exit: every domain has an evidence-based level and the next phases are re-ordered by gaps.

## Phase 1 — Foundations: the building blocks

PY data model, iterators/generators, decorators, context managers, typing, dataclasses, packaging · OO SOLID, composition, dependency injection, key patterns (Strategy, Observer, State, Adapter, Command) · EP TDD, property-based testing, fakes vs mocks · DS dynamic array, linked lists, ring buffer, hash map, heap, trees · config-driven design with validated schemas.

Greenhouse: config loader with schema validation, device registry, ring-buffered serial reader, timer heap, in-process event bus, table-driven FSM.

## Phase 2 — Kernel and concurrency

OS processes, threads, scheduling (RR, MLFQ, CFS/EEVDF), virtual memory, paging, TLB, page replacement, synchronization, deadlock, file systems · PY threading, GIL and free-threading, multiprocessing, asyncio · LX fork/exec, signals, init systems · IO pipes, Unix sockets, shared memory, message queues · AL graph algorithms (deadlock detection, dependency ordering), trees for schedulers, LRU/clock.

Greenhouse: cooperative scheduler, service supervisor with restart policies, multi-process IPC layer, simulated paging memory manager.

## Phase 3 — The hardware boundary

CA memory hierarchy, caches, pipelines, branch prediction, memory ordering, atomics, endianness, DMA · EM GPIO, UART/SPI/I2C/RS485, timing, watchdogs, binary protocol design, CRC, firmware update strategies, real-time behaviour · LX syscalls, file descriptors, epoll, /proc and /sys, device model, char drivers, device tree, libgpiod · C and Python interop (ctypes, C extensions).

Greenhouse: binary protocol codec with CRC and framing, half-duplex bus simulator, epoll-driven IO loop, cache simulator, a C component called from Python, a char-device kernel module running in QEMU.

## Phase 4 — Networks and distributed systems

NW TCP/IP, sockets, TLS, routing, DHCP, DNS, NAT, policy routing · IO MQTT 3.1.1/5 in depth (QoS, sessions, retained, LWT, shared subscriptions) · DI failure models, clocks, delivery semantics, idempotency, replication, quorums, consensus (Raft), sharding, consistent hashing, transactions and sagas.

Greenhouse: socket transport, mini MQTT broker with QoS 1 and persistent sessions, store-and-forward cloud bridge, multi-node controller cluster with Raft leader election.

## Phase 5 — Cloud, IoT and system design

CL compute/storage/database models, containers and Kubernetes, IAM and device identity, event-driven and serverless patterns, IaC, CI/CD, cost · IO provisioning, fleet management, device twins, OTA · SD estimation, caching, queues and streams, rate limiting, API design, observability, multi-region, disaster recovery.

Greenhouse: containerized fleet simulator, telemetry pipeline, provisioning and OTA services, dashboards and SLOs; full written designs for an IoT fleet platform.

## Phase 6 — Yocto and productization

YO layers, recipes, classes, bbappends, machine/distro/image configuration, sstate and task hashes, devtool, kernel configuration and device tree, SDK, licensing, SBOM, reproducibility.

Greenhouse: a custom layer that packages Greenhouse into a QEMU image with init scripts. Long builds run in the background, outside sessions.
Status: waiting on a WSL restart before environment checks.

## Phase 7 — Synthesis and mastery

Teach-back series, design documents for real work systems, deep dives chosen by remaining gaps, reading primary sources (papers, kernel docs, RFCs).

## Continuous threads (every week, every phase)

- **Algorithms practice:** one problem-solving pattern a week, applied inside the current component where possible, plus timed practice on Fridays.
- **Clean design:** a named principle or standard introduced whenever lab work warrants it; periodic refactoring katas.
- **AI proficiency ladder:**
  - A1 Prompts as specifications: context, constraints, examples, verification.
  - A2 Claude Code fluency: CLAUDE.md, memory, skills, subagents, hooks, MCP, plan mode, `/loop`; the learner builds tooling for this repo.
  - A3 Orchestration: parallel agents, workflows, evaluation loops, knowing when not to use agents.
  - A4 Building with the API: tool use, structured outputs, caching, evals; a real tool for day-to-day engineering (e.g., log triage).
- **Work tie-ins:** a weekly live "connect" moment in conversation only, never recorded (see the work boundary in `AGENTS.md`).

## Review cadence

- Weekly (Friday): progress, pace and difficulty check.
- Monthly: protocol effectiveness; roadmap re-ordering; new resources via the `resource-scout` agent.
- Quarterly: mastery snapshot in `learner/profile.md`.
