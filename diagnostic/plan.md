# Baseline Diagnostic

Goal: an evidence-based level for every domain, with no guessing about what the learner knows. Reading ahead is fine but blunts the calibration.

## Protocol (tutor)

- **Adaptive probing.** For each domain, start with an L2 question. Correct → climb (L3, L4); wrong or "don't know" → drop to L1. A domain's level boundary is found when two questions at the same level are missed. Do not ask every question; ask enough to locate the boundary with confidence.
- **Confidence on every answer** (1–5). Record calibration: correct+low confidence = under-confident; wrong+high = misconception (top priority).
- **"I don't know" is a valid, valued answer.** Guessing is discouraged; partial reasoning is welcome.
- **Answers are verbal or short code**, one question at a time. After each answer give a one- or two-line correction or confirmation, so no misconception survives. Save full teaching for the curriculum.
- **Follow-ups beat new questions:** "why?", "what breaks if…?", "where have you seen this?" reveal depth faster.
- **Record as you go** in `diagnostic/progress.md` after every answer: question ID, result (correct/partial/wrong/unknown), confidence, a short note on reasoning, and the next question. This makes the diagnostic resumable mid-domain at any point. Questions about the learner's own experience are discussed live; record only the quality of the answer, never work details (work boundary in `AGENTS.md`).
- After all rounds: fill the domain map in `learner/profile.md`, seed the review queue with every miss, and re-order `roadmap.md` by gaps.

## Rounds (~1 session each)

| Round | Verbal domains | Hands-on |
|---|---|---|
| 1 | PY, OO, EP | D1 ring buffer |
| 2 | DS, AL | D2 LRU cache, D3 service startup order |
| 3 | OS, LX | D4 bounded blocking queue |
| 4 | CA, EM, YO | D5 refactor kata |
| 5 | NW, IO, DI | — |
| 6 | SD, CL, AI | D6 design exercise |
| 7 | CP, SC, DB | — |

Hands-on labs live in `labs/diagnostic/`. Each is time-boxed to ~25 minutes; the time taken and the code quality are both evidence. The learner may run labs between sessions.

## Question bank

IDs are `DOMAIN-LEVEL.n`. Tutor-only guidance in italics.

### PY — Python

- PY-1.1 What does `def f(x=[]): x.append(1); return x` return on the second call, and why?
- PY-1.2 `is` vs `==`. Why can `a is b` be True for some equal ints and False for others?
- PY-2.1 How does a dict lookup work internally? Why must keys be hashable? What happens if a class defines `__eq__` but not `__hash__`?
- PY-2.2 Iterable vs iterator vs generator. Write a generator yielding sliding windows of size k over any iterable.
- PY-2.3 Write a parameterized `retry(max_attempts, exceptions)` decorator that preserves the wrapped function's metadata.
- PY-3.1 What does the GIL protect? When do threads help in CPython and when not? What changes with free-threaded builds?
- PY-3.2 Context manager semantics: what `__exit__` receives, how exceptions get suppressed, and `contextlib.contextmanager`.
- PY-3.3 Inside a coroutine you call `time.sleep(2)`. What happens to the event loop? How should blocking IO run under asyncio?
- PY-4.1 How does `@property` work underneath (descriptor protocol)? Data vs non-data descriptors and lookup precedence.
- PY-4.2 Explain MRO and C3 linearization with a diamond; what `super()` actually calls.
- PY-4.3 CPython memory management: refcounting, cyclic GC, `__slots__`, a real use for `weakref`.
- PY-4.4 dataclass vs NamedTuple vs Pydantic model; `typing.Protocol` vs `abc.ABC`. When each?

### OO — OOP and design

- OO-1.1 Give an example of encapsulation, inheritance, polymorphism and abstraction from code you've worked on.
- OO-2.1 State each SOLID principle and describe a real violation and its fix.
- OO-2.2 Composition vs inheritance: when is inheritance the right call?
- OO-2.3 When does DRY hurt? What is "the wrong abstraction"?
- OO-3.1 Dependency injection: what, why, and how it changes testing in Python.
- OO-3.2 State pattern vs table-driven FSM for a device state machine: trade-offs.
- OO-3.3 Config-driven architecture: what belongs in config vs code? Risks and how to mitigate them (schemas, validation, defaults).
- OO-3.4 Which of Strategy, Observer, Adapter, Command, Factory have you used, and where?
- OO-4.1 Ports and adapters (hexagonal): apply it to a hardware-dependent service so it is testable off-target.
- OO-4.2 Law of Demeter, tell-don't-ask, cohesion vs coupling; resolve the tension between YAGNI and extensibility.

### EP — Engineering practice

- EP-1.1 Unit vs integration vs system tests; the test pyramid and why.
- EP-2.1 Mock vs stub vs fake vs spy. What does over-mocking cost?
- EP-2.2 What is property-based testing, and what kind of bug does it find that example tests miss?
- EP-3.1 Error handling: exceptions vs return values, fail-fast, retries with exponential backoff and jitter (why jitter?).
- EP-3.2 Static typing in Python: generics, Protocols, `TypeVar`, what mypy strict catches.
- EP-3.3 A Python service is slow. How do you find the bottleneck (cProfile, py-spy, perf), and how do you confirm the fix?
- EP-4.1 What do you look for in a code review, in priority order? How do you manage technical debt deliberately?

### DS — Data structures

- DS-1.1 Array vs linked list operation costs; when a linked list genuinely wins.
- DS-1.2 Implement a queue with two stacks; amortized cost of dequeue.
- DS-2.1 Hash table collision strategies, load factor, resizing, and why insertion is amortized O(1).
- DS-2.2 Heap operations and costs; why is heapify O(n)?
- DS-2.3 BST vs balanced BST (AVL/red-black) vs B-tree; why B-trees for storage.
- DS-3.1 Trie and union-find: uses and complexity (path compression, union by rank).
- DS-3.2 Graph representations; when adjacency matrix vs list.
- DS-4.1 Bloom filter: false-positive behaviour and sizing intuition. Skip list vs balanced tree.
- DS-4.2 LSM tree vs B-tree: write/read/space amplification trade-offs.

### AL — Algorithms

- AL-1.1 Write binary search; state its loop invariant.
- AL-1.2 Complexity of a given nested-loop or recursive snippet (*tutor supplies one*).
- AL-2.1 Longest substring without repeating characters: approach and complexity.
- AL-2.2 BFS vs DFS: which problems call for each?
- AL-2.3 Recursion vs iteration; Python's recursion limit and how to restructure.
- AL-3.1 Dynamic programming: define state and transition for coin change; top-down vs bottom-up.
- AL-3.2 Dijkstra: how it works; why negative edges break it; what to use instead.
- AL-3.3 Backtracking: permutations with pruning.
- AL-4.1 Interval scheduling: prove the greedy choice; a problem where greedy fails.
- AL-4.2 NP-completeness intuition; what a reduction shows.

### OS — Operating systems

- OS-1.1 Process vs thread; what a context switch saves and costs.
- OS-1.2 User vs kernel mode; what happens mechanically on a syscall.
- OS-2.1 RR, priority, MLFQ, CFS: how does CFS pick the next task? What replaced it in recent kernels?
- OS-2.2 Virtual memory: page tables, TLB, minor vs major page faults.
- OS-2.3 Mutex vs spinlock vs semaphore vs condition variable; when a spinlock is right.
- OS-3.1 Coffman conditions; prevention vs avoidance vs detection.
- OS-3.2 Priority inversion and priority inheritance (a real incident).
- OS-3.3 `write()` returns success. Is the data on disk? Page cache, writeback, `fsync`, journaling.
- OS-3.4 fork, copy-on-write, exec; zombies vs orphans; what init does with orphans.
- OS-4.1 Buddy and slab allocators; internal vs external fragmentation.

### LX — Linux internals

- LX-1.1 What are /proc and /sys? Find a process's open files and memory map.
- LX-1.2 SIGTERM vs SIGKILL vs SIGHUP vs SIGCHLD; which can't be caught and why.
- LX-2.1 File descriptors, `dup2`, pipes. Difference between `cmd > out 2>&1` and `cmd 2>&1 > out`.
- LX-2.2 Boot sequence: bootloader → kernel → initramfs → init → SysV runlevels and init scripts.
- LX-2.3 A process is hung. Walk through diagnosing it (strace, /proc/PID/stack, gdb, perf).
- LX-3.1 select vs poll vs epoll; edge- vs level-triggered.
- LX-3.2 Namespaces and cgroups: how containers are built from them.
- LX-3.3 Kernel modules and char devices: `file_operations`, ioctl vs sysfs; why GPIO sysfs gave way to the GPIO char device and libgpiod.
- LX-4.1 Overcommit and the OOM killer; RSS vs VSZ vs PSS.
- LX-4.2 Device tree and udev: how hardware gets described and device nodes appear.

### CA — Computer architecture

- CA-1.1 Order-of-magnitude latencies: register, L1, L2, L3, RAM, SSD, network round trip.
- CA-1.2 Store 0x12345678 little-endian, byte by byte. Where has endianness mattered in your work?
- CA-2.1 Cache lines, locality, associativity; false sharing.
- CA-2.2 Pipelining, hazards, branch prediction; why iterating a sorted array with a branch can be faster.
- CA-2.3 Interrupts vs polling; ISR design rules; interrupt latency.
- CA-3.1 Memory ordering and barriers; what C `volatile` does and does not guarantee.
- CA-3.2 DMA and cache coherency.
- CA-3.3 ARM Cortex-A vs Cortex-M; MMU vs MPU; RISC vs CISC today.
- CA-4.1 Compare-and-swap, LL/SC, the ABA problem.
- CA-4.2 Page table walk and TLB shootdown on multicore.

### EM — Embedded and devices

- EM-1.1 Pull-up/pull-down, open-drain, active-low; why an LED can need inverted polarity.
- EM-1.2 UART vs SPI vs I2C vs RS485: wiring, duplex, addressing, speed.
- EM-2.1 Debouncing; hardware vs software watchdogs.
- EM-2.2 RS485 half-duplex: direction control, turnaround timing, contention, termination and biasing.
- EM-2.3 Bare metal vs RTOS vs embedded Linux: how you choose.
- EM-2.4 C: struct padding and alignment, `__attribute__((packed))` risks, set/clear/toggle a bit with masks.
- EM-3.1 Binary protocol design: framing, escaping, CRC vs checksum, versioning.
- EM-3.2 ADC basics: resolution, reference, sampling rate, aliasing.
- EM-3.3 Firmware update: A/B image slots, rollback, signing.
- EM-4.1 Hard vs soft real-time; PREEMPT_RT; measuring jitter.
- EM-4.2 Secure boot chain, hardware root of trust, key storage.

### YO — Yocto and builds

- YO-1.1 Yocto vs OpenEmbedded vs Poky vs BitBake; what a layer is.
- YO-2.1 Recipe anatomy: SRC_URI, do_compile, do_install, FILES, DEPENDS vs RDEPENDS.
- YO-2.2 bbappends, layer priority; machine vs distro vs image configuration.
- YO-3.1 sstate cache and task signatures; why an unexpected rebuild happens and how to find the cause.
- YO-3.2 devtool workflow; packaging a Python service with an init script (`update-rc.d` class).
- YO-4.1 Kernel customization: config fragments, patches, device tree; SDK vs eSDK.
- YO-4.2 License compliance, SBOM (SPDX), reproducible builds.

### NW — Networking

- NW-1.1 TCP vs UDP; what each layer of the TCP/IP model is responsible for.
- NW-1.2 What happens between typing `curl https://host` and receiving the response?
- NW-2.1 TCP handshake, retransmission, TIME_WAIT, keepalive, Nagle.
- NW-2.2 Routing table and metrics, default route, NAT, the DHCP exchange.
- NW-3.1 TLS 1.3 handshake; certificate chains; mutual TLS.
- NW-3.2 Sockets: blocking vs non-blocking, listen backlog, `SO_REUSEADDR`.
- NW-4.1 Congestion control; head-of-line blocking; what QUIC changes.
- NW-4.2 Policy routing with multiple tables; ethernet/cellular failover design.

### IO — IPC, MQTT and IoT

- IO-1.1 Pipes, FIFOs, Unix sockets, shared memory, message queues, D-Bus: trade-offs.
- IO-1.2 MQTT broker, topics, wildcards, QoS 0/1/2.
- IO-2.1 Retained messages, last will, clean vs persistent sessions, keepalive.
- IO-2.2 MQTT 5 additions: session expiry, receive maximum, shared subscriptions, reason codes, user properties.
- IO-3.1 QoS 1 with an offline client: what actually guarantees delivery, and where it breaks.
- IO-3.2 Device provisioning, identity, device twin/shadow, OTA at fleet scale.
- IO-3.3 Edge vs cloud processing; store-and-forward design.
- IO-4.1 Scaling brokers (clustering, bridging); topic design for multi-tenant fleets; MQTT vs AMQP vs CoAP vs DDS.

### DI — Distributed systems

- DI-1.1 Why distributed systems are hard: partial failure, unbounded latency, no global clock.
- DI-2.1 CAP and PACELC; linearizable vs sequential vs causal vs eventual consistency.
- DI-2.2 At-most/at-least/exactly-once; idempotency keys.
- DI-2.3 Lamport vs vector clocks.
- DI-3.1 Leader-follower, multi-leader, leaderless quorums (R + W > N).
- DI-3.2 Raft: leader election and log replication; why majorities.
- DI-3.3 Consistent hashing; hot shards.
- DI-4.1 2PC and its failure modes; sagas; transactional outbox.
- DI-4.2 Failure detection, split brain, fencing tokens.

### SD — System design

- SD-1.1 Vertical vs horizontal scaling; load balancers; why stateless services.
- SD-2.1 Cache-aside, write-through, write-back; invalidation strategies.
- SD-2.2 SQL vs NoSQL; indexes; when Redis fits and its persistence modes (RDB, AOF).
- SD-2.3 Message queue vs log-based stream; backpressure.
- SD-3.1 Estimate: 100k devices, one 500-byte message every 10 s. Throughput, daily storage, peak headroom.
- SD-3.2 Token bucket vs leaky bucket vs sliding window rate limiting.
- SD-3.3 REST vs gRPC vs MQTT for device APIs; versioning; pagination.
- SD-4.1 Logs, metrics, traces; SLI/SLO/error budgets.
- SD-4.2 Multi-region design; RPO/RTO; disaster recovery.

### CL — Cloud architecture

- CL-1.1 IaaS/PaaS/SaaS/serverless; regions and availability zones.
- CL-2.1 Compute options (VMs, containers, functions); storage types (object, block, file).
- CL-2.2 Container images and layers; Kubernetes pods, deployments, services.
- CL-3.1 IAM least privilege; secrets management; per-device X.509 identity.
- CL-3.2 Event-driven cloud: queues, pub/sub, stream processing; serverless cold starts.
- CL-3.3 Infrastructure as code; CI/CD pipelines.
- CL-4.1 Cost-aware architecture; multi-tenant isolation; well-architected trade-offs.

### AI — AI-assisted engineering

- AI-1.1 How an LLM produces text: tokens, context window, next-token prediction; why it hallucinates.
- AI-2.1 What makes a strong prompt for an engineering task? Take a weak prompt and improve it (*tutor supplies one*).
- AI-2.2 Claude Code: CLAUDE.md, memory, skills, subagents, hooks, MCP, plan mode — what each is for.
- AI-3.1 Agentic workflows: decomposition, parallel subagents, verification loops; when not to use agents.
- AI-3.2 Verifying AI output: tests as oracle, review, failure modes (sycophancy, confident errors).
- AI-4.1 Building with the API: tool use, structured outputs, prompt caching, evals.
- AI-4.2 RAG vs fine-tuning vs long context: when each.

### CP — C and systems programming

- CP-1.1 Stack vs heap vs static storage and their lifetimes; what happens when a function returns a pointer to a local.
- CP-1.2 Pointer arithmetic and arrays; `sizeof` of an array vs of an array parameter.
- CP-2.1 Undefined behaviour: common sources (signed overflow, out-of-bounds, use-after-free, strict aliasing) and why compilers exploit it.
- CP-2.2 Preprocessor → compiler → assembler → linker; static vs shared libraries; symbols and relocations.
- CP-2.3 `const`, `volatile`, `static` (file vs function scope), `extern`.
- CP-3.1 Valgrind vs AddressSanitizer vs UBSan: what each catches.
- CP-3.2 Find a crash from a core dump with gdb, step by step.
- CP-3.3 Make and CMake: incremental builds, dependency tracking; cross-compiling against a sysroot.
- CP-4.1 ABIs and calling conventions; how Python's `ctypes` calls into C.
- CP-4.2 Rust's ownership model vs C: which bug classes it removes and at what cost.

### SC — Security

- SC-1.1 Confidentiality, integrity, availability; authentication vs authorization.
- SC-2.1 Symmetric vs asymmetric cryptography; hash vs MAC vs signature, and where each is used.
- SC-2.2 Injection, buffer overflow, path traversal, unsafe deserialization: causes and mitigations.
- SC-2.3 Storing secrets on a device and in services; rotation.
- SC-3.1 Threat-model a networked embedded device with STRIDE.
- SC-3.2 Secure boot and signed updates: chain of trust, rollback protection.
- SC-3.3 Coverage-guided fuzzing: how it works; what to fuzz in a binary protocol parser.
- SC-4.1 SBOMs and vulnerability management (CVE triage) for an embedded Linux product.
- SC-4.2 Timing side channels; constant-time comparison.

### DB — Databases

- DB-1.1 Relational model, keys, normalization basics.
- DB-2.1 How a B-tree index speeds up a query; when an index hurts.
- DB-2.2 ACID; isolation levels and the anomalies each permits.
- DB-3.1 MVCC vs lock-based concurrency control.
- DB-3.2 Time-series data: storage layout, retention, downsampling.
- DB-3.3 Key-value stores: in-memory vs persistent, durability trade-offs.
- DB-4.1 Write-ahead logging and crash recovery.
- DB-4.2 Reading a query plan (`EXPLAIN`).
