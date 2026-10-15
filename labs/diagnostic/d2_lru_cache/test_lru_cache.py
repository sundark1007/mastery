import pathlib

import pytest

from lru_cache import LRUCache


def test_rejects_non_positive_capacity():
    with pytest.raises(ValueError):
        LRUCache(0)


def test_get_missing_returns_default():
    cache = LRUCache(2)
    assert cache.get("k") is None
    assert cache.get("k", 42) == 42


def test_evicts_least_recently_used():
    cache = LRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)
    assert "a" not in cache
    assert cache.get("b") == 2
    assert cache.get("c") == 3


def test_get_refreshes_recency():
    cache = LRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    cache.get("a")
    cache.put("c", 3)
    assert "b" not in cache
    assert cache.get("a") == 1


def test_put_existing_updates_and_refreshes():
    cache = LRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("a", 10)
    cache.put("c", 3)
    assert len(cache) == 2
    assert cache.get("a") == 10
    assert "b" not in cache


def test_membership_does_not_refresh():
    cache = LRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    assert "a" in cache
    cache.put("c", 3)
    assert "a" not in cache


def test_capacity_one():
    cache = LRUCache(1)
    cache.put("a", 1)
    cache.put("b", 2)
    assert len(cache) == 1
    assert cache.get("a") is None
    assert cache.get("b") == 2


def test_falsy_values_are_stored():
    cache = LRUCache(2)
    cache.put("zero", 0)
    cache.put("none", None)
    assert cache.get("zero", "missing") == 0
    assert cache.get("none", "missing") is None
    assert len(cache) == 2


def test_long_sequence_matches_reference():
    cache = LRUCache(3)
    reference: list[tuple[int, int]] = []
    for step in range(200):
        key = (step * 7) % 5
        if step % 3:
            cache.put(key, step)
            reference = [kv for kv in reference if kv[0] != key] + [(key, step)]
            reference = reference[-3:]
        else:
            found = [v for k, v in reference if k == key]
            assert cache.get(key) == (found[0] if found else None)
            if found:
                reference = [kv for kv in reference if kv[0] != key] + [(key, found[0])]
    assert len(cache) == len(reference)


def test_no_shortcut_imports():
    source = (pathlib.Path(__file__).parent / "lru_cache.py").read_text()
    assert "OrderedDict" not in source
    assert "functools" not in source
