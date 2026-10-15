"""D3: service startup order.

A supervisor must start services so that every service starts after all services it requires.

Spec:
- ``startup_order(requires)``: ``requires`` maps a service name to the names it requires.
  Services that appear only as requirements are included too.
- Return a list where each service appears after all of its requirements.
- Deterministic: whenever several services are ready to start, pick the alphabetically smallest.
- On a dependency cycle raise ``CycleError`` whose ``cycle`` attribute lists the services on the
  cycle in dependency order, closed (first == last), e.g. ``["a", "b", "c", "a"]`` meaning a
  requires b, b requires c, c requires a. Any rotation of the cycle is acceptable.
- No ``graphlib``.
"""

from collections.abc import Iterable, Mapping


class CycleError(Exception):
    def __init__(self, cycle: list[str]) -> None:
        super().__init__(" -> ".join(cycle))
        self.cycle = cycle


def startup_order(requires: Mapping[str, Iterable[str]]) -> list[str]:
    raise NotImplementedError
