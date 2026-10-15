import pathlib

import pytest

from service_order import CycleError, startup_order


def assert_valid(order, requires):
    position = {name: i for i, name in enumerate(order)}
    assert len(position) == len(order), "duplicates in order"
    for service, deps in requires.items():
        for dep in deps:
            assert position[dep] < position[service], f"{dep} must start before {service}"


def test_empty():
    assert startup_order({}) == []


def test_linear_chain():
    requires = {"cloud": ["ipc"], "ipc": ["broker"], "broker": []}
    assert startup_order(requires) == ["broker", "ipc", "cloud"]


def test_includes_requirement_only_services():
    order = startup_order({"app": ["redis", "broker"]})
    assert order == ["broker", "redis", "app"]


def test_alphabetical_tie_break():
    requires = {"d": ["a"], "c": ["a"], "b": ["a"], "a": []}
    assert startup_order(requires) == ["a", "b", "c", "d"]


def test_tie_break_applies_to_newly_ready_services():
    requires = {"z": [], "b": ["z"], "a": ["z"], "m": []}
    assert startup_order(requires) == ["m", "z", "a", "b"]


def test_diamond():
    requires = {
        "rules": ["ipc", "data"],
        "ipc": ["broker"],
        "data": ["broker", "redis"],
        "broker": [],
        "redis": [],
    }
    order = startup_order(requires)
    assert_valid(order, requires)
    assert order == ["broker", "ipc", "redis", "data", "rules"]


def _assert_cycle(cycle, requires):
    assert cycle[0] == cycle[-1]
    for a, b in zip(cycle, cycle[1:]):
        assert b in requires[a], f"{a} does not require {b}"


def test_cycle_detected_with_path():
    requires = {"a": ["b"], "b": ["c"], "c": ["a"], "d": []}
    with pytest.raises(CycleError) as exc:
        startup_order(requires)
    cycle = exc.value.cycle
    _assert_cycle(cycle, requires)
    assert set(cycle) == {"a", "b", "c"}


def test_self_dependency_is_a_cycle():
    with pytest.raises(CycleError) as exc:
        startup_order({"a": ["a"]})
    assert exc.value.cycle == ["a", "a"]


def test_cycle_reachable_from_acyclic_part():
    requires = {"app": ["x"], "x": ["y"], "y": ["z"], "z": ["x"]}
    with pytest.raises(CycleError) as exc:
        startup_order(requires)
    _assert_cycle(exc.value.cycle, requires)
    assert "app" not in exc.value.cycle


def test_large_chain_no_recursion_limit():
    n = 5000
    requires = {f"s{i:05d}": [f"s{i - 1:05d}"] for i in range(1, n)}
    order = startup_order(requires)
    assert order[0] == "s00000" and order[-1] == f"s{n - 1:05d}"


def test_no_graphlib():
    source = (pathlib.Path(__file__).parent / "service_order.py").read_text()
    assert "graphlib" not in source
