"""D4: bounded blocking queue.

Spec:
- ``BoundedQueue(capacity)``: capacity must be a positive int, else ``ValueError``.
- ``put(item, timeout=None)``: block while full. ``timeout`` in seconds; raise ``TimeoutError``
  if still full when it expires. ``None`` waits forever.
- ``get(timeout=None)``: block while empty; same timeout semantics. FIFO order.
- ``len(q)``: current number of items.
- Thread-safe for many producers and consumers; every item is delivered exactly once.
- Use ``threading`` primitives only; no ``queue`` module. Timeouts must hold across
  spurious wakeups.
"""


class BoundedQueue:
    def __init__(self, capacity: int) -> None:
        raise NotImplementedError
