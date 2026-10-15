import json
import time

import pytest

from event_router import handle


def msg(sensor_type, value, dev="dev-1"):
    return json.dumps({"type": sensor_type, "value": value, "id": dev})


@pytest.mark.parametrize(
    "sensor_type, value, level, notify",
    [
        ("pressure", 51, "critical", ["local", "cloud"]),
        ("temp", 71, "critical", ["local", "cloud"]),
        ("temp", 61, "warning", ["cloud"]),
        ("door", 1, "warning", ["cloud"]),
        ("battery", 19, "warning", ["cloud"]),
    ],
)
def test_events(sensor_type, value, level, notify):
    before = time.time()
    out = handle(msg(sensor_type, value))
    assert out["level"] == level
    assert out["dev"] == "dev-1"
    assert out["notify"] == notify
    assert before <= out["ts"] <= time.time()


@pytest.mark.parametrize(
    "sensor_type, value",
    [("pressure", 50), ("temp", 59), ("temp", 60), ("door", 0), ("battery", 20)],
)
def test_no_event(sensor_type, value):
    assert handle(msg(sensor_type, value)) is None


def test_boundaries():
    assert handle(msg("temp", 70))["level"] == "warning"
    assert handle(msg("temp", 70.5))["level"] == "critical"
    assert handle(msg("pressure", 50.5))["level"] == "critical"


def test_unknown_type_raises():
    with pytest.raises(Exception):
        handle(msg("humidity", 99))


def test_notify_lists_are_independent():
    first = handle(msg("pressure", 99))
    first["notify"].append("tampered")
    assert handle(msg("pressure", 99))["notify"] == ["local", "cloud"]
