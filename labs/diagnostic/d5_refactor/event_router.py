"""D5: refactor kata.

This module routes readings from a building's environmental sensors. It works, and the tests
pin its behaviour. Refactor it so it is clean, modular, config-driven and DRY, without changing
behaviour visible to the tests. Then explain each change and the principle behind it.

Public API to preserve: ``handle(msg: str) -> dict | None``. It raises an exception for an
unknown sensor type.
"""

import json
import time


def handle(msg):
    d = json.loads(msg)
    if d["type"] == "pressure":
        if d["value"] > 50:
            out = {"level": "critical", "dev": d["id"], "ts": time.time(), "notify": ["local", "cloud"]}
            print("CRITICAL", d["id"])
            return out
        else:
            return None
    elif d["type"] == "temp":
        if d["value"] > 70:
            out = {"level": "critical", "dev": d["id"], "ts": time.time(), "notify": ["local", "cloud"]}
            print("CRITICAL", d["id"])
            return out
        elif d["value"] > 60:
            out = {"level": "warning", "dev": d["id"], "ts": time.time(), "notify": ["cloud"]}
            print("WARNING", d["id"])
            return out
        else:
            return None
    elif d["type"] == "door":
        if d["value"] == 1:
            out = {"level": "warning", "dev": d["id"], "ts": time.time(), "notify": ["cloud"]}
            print("WARNING", d["id"])
            return out
        return None
    elif d["type"] == "battery":
        if d["value"] < 20:
            out = {"level": "warning", "dev": d["id"], "ts": time.time(), "notify": ["cloud"]}
            print("WARNING", d["id"])
            return out
        return None
    else:
        raise Exception("bad type " + d["type"])
