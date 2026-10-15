"""D2: least-recently-used cache.

Spec:
- ``LRUCache(capacity)``: capacity must be a positive int, else ``ValueError``.
- ``get(key, default=None)``: return the value and mark it most recently used; ``default`` if absent.
- ``put(key, value)``: insert or update, marking it most recently used; evict the least
  recently used entry when over capacity.
- ``len(cache)`` and ``key in cache``; membership does not affect recency.
- ``get`` and ``put`` are O(1). Build the recency order yourself: no ``OrderedDict``,
  no ``functools``.
"""


class LRUCache:
    def __init__(self, capacity: int) -> None:
        raise NotImplementedError
