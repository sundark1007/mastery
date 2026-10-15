import pytest

from ring_buffer import RingBuffer


@pytest.mark.parametrize("capacity", [0, -1])
def test_rejects_non_positive_capacity(capacity):
    with pytest.raises(ValueError):
        RingBuffer(capacity)


def test_fifo_order():
    buf = RingBuffer(3)
    for i in range(3):
        buf.push(i)
    assert [buf.pop() for _ in range(3)] == [0, 1, 2]


def test_overwrites_oldest_when_full():
    buf = RingBuffer(3)
    for i in range(5):
        buf.push(i)
    assert len(buf) == 3
    assert list(buf) == [2, 3, 4]
    assert buf.pop() == 2


def test_pop_empty_raises():
    buf = RingBuffer(2)
    with pytest.raises(IndexError):
        buf.pop()
    buf.push("a")
    buf.pop()
    with pytest.raises(IndexError):
        buf.pop()


def test_iteration_does_not_consume():
    buf = RingBuffer(4)
    for c in "abc":
        buf.push(c)
    assert list(buf) == ["a", "b", "c"]
    assert len(buf) == 3


def test_is_full_tracks_state():
    buf = RingBuffer(2)
    assert not buf.is_full
    buf.push(1)
    buf.push(2)
    assert buf.is_full
    buf.pop()
    assert not buf.is_full


def test_is_full_is_read_only():
    buf = RingBuffer(1)
    with pytest.raises(AttributeError):
        buf.is_full = True


def test_wraparound_interleaved():
    buf = RingBuffer(3)
    out = []
    for i in range(10):
        buf.push(i)
        if i % 2:
            out.append(buf.pop())
    assert out == [0, 1, 3, 5, 7]
    assert list(buf) == [8, 9]


def test_capacity_one():
    buf = RingBuffer(1)
    buf.push("x")
    buf.push("y")
    assert list(buf) == ["y"]
    assert buf.pop() == "y"
    assert len(buf) == 0
