# D6: Design exercise — cold-chain monitoring platform

Write your design in `design.md` in this folder (~40 minutes). Diagrams in ASCII or Mermaid are fine. Then defend it in a discussion.

## Problem

A logistics company monitors temperature-sensitive goods (vaccines, food) across 100,000 edge hubs installed in warehouses and refrigerated trucks. Each hub collects readings from up to 64 wireless and wired sensors (temperature, humidity, door, power).

- Each hub sends a heartbeat every 30 s and sensor readings as they change (average 1 per sensor per 10 min, bursts when a door opens or power fails).
- A temperature excursion must reach the responsible operator within 2 s, end to end (p99), even while parts of the system are degraded.
- Operators send commands to a single hub or sensor (setpoint change, configuration, firmware update) and need confirmation of execution.
- Hubs run on cellular or ethernet with intermittent connectivity (trucks lose coverage); they must not lose excursion events while offline.
- Twelve months of readings must be queryable per shipment and per site for compliance audits.

## Cover

1. Requirements: functional, non-functional, explicit assumptions.
2. Back-of-envelope: message rates, bandwidth, storage per day and per year.
3. High-level architecture and the data flow for (a) an excursion event, (b) a command.
4. Protocols and message design: delivery guarantees, ordering, idempotency, schema versioning.
5. Edge design: store-and-forward, reconnect behaviour, clock handling.
6. Data storage choices and why.
7. Failure modes and how the design degrades; what you monitor (SLIs/SLOs).
8. Security: device identity, authentication, authorization, secret rotation.
9. Firmware update at fleet scale: rollout, rollback, safety.
10. What you would build first, and what you consciously left out.
