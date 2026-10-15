import pathlib
import threading
import time

import pytest

from bounded_queue import BoundedQueue


def test_rejects_non_positive_capacity():
    with pytest.raises(ValueError):
        BoundedQueue(0)


def test_fifo_single_thread():
    q = BoundedQueue(3)
    for i in range(3):
        q.put(i)
    assert len(q) == 3
    assert [q.get() for _ in range(3)] == [0, 1, 2]


def test_get_times_out_when_empty():
    q = BoundedQueue(1)
    start = time.monotonic()
    with pytest.raises(TimeoutError):
        q.get(timeout=0.2)
    assert 0.15 <= time.monotonic() - start < 1.0


def test_put_times_out_when_full():
    q = BoundedQueue(1)
    q.put("a")
    start = time.monotonic()
    with pytest.raises(TimeoutError):
        q.put("b", timeout=0.2)
    assert 0.15 <= time.monotonic() - start < 1.0
    assert len(q) == 1


def test_put_blocks_until_space():
    q = BoundedQueue(1)
    q.put("first")
    done = threading.Event()

    def producer():
        q.put("second")
        done.set()

    t = threading.Thread(target=producer)
    t.start()
    assert not done.wait(0.2), "put should block while full"
    assert q.get() == "first"
    assert done.wait(1.0)
    assert q.get() == "second"
    t.join()


def test_get_blocks_until_item():
    q = BoundedQueue(1)
    result = []
    t = threading.Thread(target=lambda: result.append(q.get()))
    t.start()
    time.sleep(0.1)
    assert not result
    q.put("x")
    t.join(1.0)
    assert result == ["x"]


def test_many_producers_consumers_exactly_once():
    q = BoundedQueue(4)
    producers, consumers, per_producer = 4, 4, 500
    received = []
    lock = threading.Lock()
    sentinel = object()

    def produce(pid):
        for i in range(per_producer):
            q.put((pid, i))

    def consume():
        while True:
            item = q.get(timeout=5)
            if item is sentinel:
                return
            with lock:
                received.append(item)

    threads = [threading.Thread(target=produce, args=(p,)) for p in range(producers)]
    threads += [threading.Thread(target=consume) for _ in range(consumers)]
    for t in threads:
        t.start()
    for t in threads[:producers]:
        t.join(10)
    for _ in range(consumers):
        q.put(sentinel, timeout=5)
    for t in threads[producers:]:
        t.join(10)

    assert sorted(received) == sorted((p, i) for p in range(producers) for i in range(per_producer))
    for pid in range(producers):
        seq = [i for p, i in received if p == pid]
        assert seq == sorted(seq), "per-producer FIFO order violated"


def test_no_queue_module():
    source = (pathlib.Path(__file__).parent / "bounded_queue.py").read_text()
    assert "import queue" not in source and "from queue" not in source
