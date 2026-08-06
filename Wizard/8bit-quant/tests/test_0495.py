python
import pytest
from src_0495 import task_func

def test_task_func():
    epoch_milliseconds = 1627262400000
    seed = 0
    timezones = ["UTC"]

    event_schedule = task_func(epoch_milliseconds, seed, timezones)

    assert isinstance(event_schedule, dict)
    assert len(event_schedule) == 1
    assert list(event_schedule.keys())[0] == "John"
    assert isinstance(event_schedule["John"], list)
    assert len(event_schedule["John"]) == 1
    assert isinstance(event_schedule["John"][0], dict)
    assert set(event_schedule["John"][0].keys()) == {"date", "time", "timezone"}
    assert event_schedule["John"][0]["date"] == "2021-07-28"
    assert event_schedule["John"][0]["time"] == "00:00:00"
    assert event_schedule["John"][0]["timezone"] == "UTC"