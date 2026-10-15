# Diagnostic Labs

Each lab is time-boxed to ~25 minutes. Implement the stub, then say `check`. Speed, correctness and code quality are all evidence; don't optimize for passing tests alone.

| Lab | Focus |
|---|---|
| D1 `d1_ring_buffer` | Data structures, Python data model, API design |
| D2 `d2_lru_cache` | Hash map + doubly linked list, O(1) design |
| D3 `d3_service_order` | Graph algorithms, cycle detection, determinism |
| D4 `d4_bounded_queue` | Concurrency primitives, condition variables, timeouts |
| D5 `d5_refactor` | Clean code, config-driven design, DRY, testability |
| D6 `d6_design` | Written system design |

Rules: standard library only; no `collections.OrderedDict`, `functools.lru_cache`, `queue` or `graphlib` where they would trivialize the lab.

Run one lab: `~/.venvs/mastery/bin/python -m pytest labs/diagnostic/d1_ring_buffer`
