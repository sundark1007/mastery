# Roadmap

A living plan. Phases set direction, not deadlines; order and depth adapt to evidence in `learner/profile.md`. Changes are recorded in the journal.

## Spine project: Fleet

A simulated datacenter server fleet, built in Python (later partly in C and packaged with Yocto). Three subsystems grow together, so every concept ends up as working, tested code inside one coherent system:

- **Node controller:** the embedded management controller in every server: sensors, fan control, power, watchdog, firmware updates, management API.
- **FleetStore:** a distributed storage engine built from scratch (log-structured storage, replication, sharding) that holds fleet state and telemetry.
- **Control plane:** fleet-wide services: inventory, telemetry pipeline, alerting, safe firmware rollouts.

All design comes from first principles and public standards; see the work boundary in `AGENTS.md`.

```text
 server x N                                     control plane
 +--------------------------------+            +--------------------------------+
 | sensors -> bus -> node agent   |-- MQTT --->| ingest -> FleetStore cluster   |
 | (I2C/PMBus) (codec)  (FSMs)    |<-- REST ---| inventory, rollouts, alerts    |
 | supervisor, watchdog, updates  |            | (Raft, sharding, replication)  |
 +--------------------------------+            +--------------------------------+
```

## Domain codes

PY Python · OO OOP & design · EP engineering practice (testing, typing, clean code) · DS data structures · AL algorithms · OS operating systems · LX Linux internals · CA computer architecture · EM embedded & devices · YO Yocto & builds · NW networking · DI distributed systems · SD system design · CL cloud architecture · IO IPC, MQTT & IoT · AI AI-assisted engineering · CP C and systems programming · SC security · DB databases

## Phase 0 — Baseline

- Adaptive diagnostic across all domains (`diagnostic/plan.md`): verbal rounds, hands-on labs and a design exercise.
- Lab environment in WSL; learning protocol tuned to the learner.
- Exit: every domain has an evidence-based level and the next phases are re-ordered by gaps.

## Phase 1 — Foundations: the building blocks

PY data model, iterators/generators, decorators, context managers, typing, dataclasses, packaging · OO SOLID, composition, dependency injection, key patterns (Strategy, Observer, State, Adapter, Command) · EP TDD, property-based testing, fakes vs mocks · DS dynamic array, linked lists, ring buffer, hash map, heap, trees · config-driven design with validated schemas.

Fleet: node-agent config schema, sensor registry, ring-buffered samples, polling timer heap, event bus, table-driven fan-control FSM · FleetStore: skip-list memtable, bloom filter, sorted-table file format.

## Phase 2 — Kernel and concurrency

OS processes, threads, scheduling (RR, MLFQ, CFS/EEVDF), virtual memory, paging, TLB, page replacement, synchronization, deadlock, file systems · PY threading, GIL and free-threading, multiprocessing, asyncio · LX fork/exec, signals, init systems · IO pipes, Unix sockets, shared memory, message queues · AL graph algorithms (deadlock detection, dependency ordering), trees for schedulers, LRU/clock.

Fleet: agent scheduler, daemon supervisor with restart policies, inter-daemon IPC, simulated paging memory manager · FleetStore: write-ahead log with fsync semantics and crash recovery, background compaction threads, mmap-based reads.

## Phase 3 — The hardware boundary

CA memory hierarchy, caches, pipelines, branch prediction, memory ordering, atomics, endianness, DMA · EM GPIO, UART/SPI/I2C/RS485, timing, watchdogs, binary protocol design, CRC, firmware update strategies, real-time behaviour · LX syscalls, file descriptors, epoll, /proc and /sys, device model, char drivers, device tree, libgpiod · C and Python interop (ctypes, C extensions).

Fleet: simulated I2C/PMBus sensor bus, binary command protocol with CRC and framing, epoll-driven IO loop, cache simulator, a C sensor driver called from Python, an hwmon-style kernel module in QEMU · FleetStore: on-disk block format (endianness, checksums), cache-friendly layout, page-cache-aware IO.

## Phase 4 — Networks and distributed systems

NW TCP/IP, sockets, TLS, routing, DHCP, DNS, NAT, policy routing · IO MQTT 3.1.1/5 in depth (QoS, sessions, retained, LWT, shared subscriptions) · DI failure models, clocks, delivery semantics, idempotency, replication, quorums, consensus (Raft), sharding, consistent hashing, transactions and sagas.

Fleet: Redfish-style REST management API, mini MQTT broker with QoS 1 and persistent sessions for telemetry, store-and-forward on the node · FleetStore: Raft replication, consistent-hash sharding and rebalancing, quorum reads and writes, anti-entropy with Merkle trees; the control plane runs on it.

## Phase 5 — Cloud, IoT and system design

DB relational modelling, indexes, transactions and isolation, MVCC, write-ahead logging, time-series and key-value storage · CL compute/storage/database models, containers and Kubernetes, IAM and device identity, event-driven and serverless patterns, IaC, CI/CD, cost · IO provisioning, fleet management, device twins, OTA · SD estimation, caching, queues and streams, rate limiting, API design, observability, multi-region, disaster recovery.

Fleet: containerized fleet simulator at scale, telemetry pipeline with downsampling and retention, canary firmware rollouts with automatic rollback, inventory and provisioning, dashboards and SLOs · FleetStore: tiered storage to object storage, backups, multi-region replication (RPO/RTO); full written designs for fleet-scale systems.

## Phase 6 — Yocto and productization

YO layers, recipes, classes, bbappends, machine/distro/image configuration, sstate and task hashes, devtool, kernel configuration and device tree, SDK, licensing, SBOM, reproducibility.

Fleet: a custom layer that packages the node controller (agent, drivers, init scripts) into a QEMU image structured like open-source server-management firmware, plus a FleetStore node image. Long builds run in the background, outside sessions.
Environment: release 6.0 (wrynose) via `bitbake-setup`; see `docs/setup.md`.

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
- **System design:** a design discussion every other Friday from Phase 1, scaled to the current phase, so design thinking grows all year instead of waiting for Phase 5.
- **C and systems programming:** a C exercise most weeks mirroring the current concept (memory layout, pointers, undefined behaviour, linking, build systems, gdb, sanitizers); Rust as a later elective.
- **Debugging and performance:** systematic debugging, profilers (cProfile, py-spy, perf), tracing (strace, ftrace, eBPF), gdb; every phase includes at least one deliberate find-the-bug and find-the-bottleneck lab.
- **Security:** threat modelling, cryptography fundamentals, secure coding, fuzzing, secure boot and update chains, SBOMs and vulnerability handling, applied to each Fleet component.
- **Technical communication:** explain-backs every session; a short design doc or architecture decision record for each phase milestone.
- **Yocto:** each phase milestone is packaged into the Fleet images (recipes, init scripts, kernel modules), so build-system skill grows continuously; Phase 6 is the deep dive.
- **Work tie-ins:** a weekly live "connect" moment in conversation only, never recorded (see the work boundary in `AGENTS.md`).

## Horizon (forecast, revised quarterly)

At about 5 hours a week (roughly 230 hours a year), the first year typically reaches through Phase 4 at mastery depth, with every continuous thread running throughout. Phases 5–7 form year two. Indicative pacing: Q1 Phases 0–1, Q2 Phase 2, Q3 Phase 3, Q4 Phase 4. The diagnostic replaces this forecast with evidence; strong domains compress, weak ones expand.

## Review cadence

- Weekly (Friday): progress, pace and difficulty check.
- Monthly: protocol effectiveness; roadmap re-ordering; new resources via the `resource-scout` agent.
- Quarterly: mastery snapshot in `learner/profile.md`.
