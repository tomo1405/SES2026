import pytest
from src_0495 import task_func
import pytz
import re
from faker import Faker

def test_task_func_with_valid_utc_timezone():
    epoch_milliseconds = 1633072800000  # Example epoch milliseconds for 2021-10-01T00:00:00Z
    result = task_func(epoch_milliseconds, seed=0, timezones=["UTC"])
    assert isinstance(result, dict)
    event_name = list(result.keys())[0]
    assert isinstance(event_name, str)
    event_schedule = result[event_name]
    assert isinstance(event_schedule, list)
    assert len(event_schedule) == 1
    event_details = event_schedule[0]
    assert isinstance(event_details, dict)
    assert "date" in event_details
    assert "time" in event_details
    assert "timezone" in event_details
    assert event_details["timezone"] == "UTC"

def test_task_func_with_valid_utc_offset_timezone():
    epoch_milliseconds = 1633072800000  # Example epoch milliseconds for 2021-10-01T00:00:00Z
    result = task_func(epoch_milliseconds, seed=0, timezones=["UTC+02:00"])
    assert isinstance(result, dict)
    event_name = list(result.keys())[0]
    assert isinstance(event_name, str)
    event_schedule = result[event_name]
    assert isinstance(event_schedule, list)
    assert len(event_schedule) == 1
    event_details = event_schedule[0]
    assert isinstance(event_details, dict)
    assert "date" in event_details
    assert "time" in event_details
    assert "timezone" in event_details
    assert event_details["timezone"] == "UTC+02:00"

def test_task_func_with_invalid_timezone():
    epoch_milliseconds = 1633072800000  # Example epoch milliseconds for 2021-10-01T00:00:00Z
    result = task_func(epoch_milliseconds, seed=0, timezones=["INVALID/TIMEZONE"])
    assert isinstance(result, dict)
    event_name = list(result.keys())[0]
    assert isinstance(event_name, str)
    event_schedule = result[event_name]
    assert isinstance(event_schedule, list)
    assert len(event_schedule) == 1
    event_details = event_schedule[0]
    assert isinstance(event_details, dict)
    assert "date" in event_details
    assert "time" in event_details
    assert "timezone" in event_details
    assert event_details["timezone"] == "UTC"

def test_task_func_with_no_timezones():
    epoch_milliseconds = 1633072800000  # Example epoch milliseconds for 2021-10-01T00:00:00Z
    result = task_func(epoch_milliseconds, seed=0, timezones=[])
    assert isinstance(result, dict)
    event_name = list(result.keys())[0]
    assert isinstance(event_name, str)
    event_schedule = result[event_name]
    assert isinstance(event_schedule, list)
    assert len(event_schedule) == 1
    event_details = event_schedule[0]
    assert isinstance(event_details, dict)
    assert "date" in event_details
    assert "time" in event_details
    assert "timezone" in event_details
    assert event_details["timezone"] == "UTC"

def test_task_func_with_multiple_timezones():
    epoch_milliseconds = 1633072800000  # Example epoch milliseconds for 2021-10-01T00:00:00Z
    result = task_func(epoch_milliseconds, seed=0, timezones=["UTC", "UTC+01:00", "America/New_York"])
    assert isinstance(result, dict)
    event_name = list(result.keys())[0]
    assert isinstance(event_name, str)
    event_schedule = result[event_name]
    assert isinstance(event_schedule, list)
    assert len(event_schedule) == 1
    event_details = event_schedule[0]
    assert isinstance(event_details, dict)
    assert "date" in event_details
    assert "time" in event_details
    assert "timezone" in event_details
    assert event_details["timezone"] in ["UTC", "UTC+01:00", "America/New_York"]