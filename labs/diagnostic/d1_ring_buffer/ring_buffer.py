"""D1: fixed-capacity ring buffer.

Spec:
- ``RingBuffer(capacity)``: capacity must be a positive int, else ``ValueError``.
- ``push(item)``: append; when full, overwrite the oldest item.
- ``pop()``: remove and return the oldest item; ``IndexError`` if empty.
- ``len(buf)``: number of stored items.
- ``iter(buf)``: oldest to newest, without consuming.
- ``is_full``: read-only property.
- All operations O(1) except iteration. No ``collections.deque``.
"""


class RingBuffer:
    def __init__(self, capacity: int) -> None:
        raise NotImplementedError
