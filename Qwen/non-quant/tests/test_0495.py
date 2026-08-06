import pytest
from src_0495 import task_func
import pytz
import re
from faker import Faker

def test_task_func_with_default_parameters():
    epoch_milliseconds = 1672531200000  # Example epoch milliseconds for January 1, 2023
    result = task_func(epoch_milliseconds)
    assert isinstance(result, dict)
    event_name = list(result.keys())[0]
    assert isinstance(event_name, str)
    event_details = result[event_name][0]
    assert isinstance(event_details, dict)
    assert isinstance(event_details["date"], datetime.date)
    assert isinstance(event_details["time"], datetime.time)
    assert event_details["timezone"] == "UTC"

def test_task_func_with_custom_seed_and_timezone():
    epoch_milliseconds = 1672531200000  # Example epoch milliseconds for January 1, 2023
    seed = 42
    timezones = ["America/New_York", "UTC+02:00"]
    result = task_func(epoch_milliseconds, seed=seed, timezones=timezones)
    assert isinstance(result, dict)
    event_name = list(result.keys())[0]
    assert isinstance(event_name, str)
    event_details = result[event_name][0]
    assert isinstance(event_details, dict)
    assert isinstance(event_details["date"], datetime.date)
    assert isinstance(event_details["time"], datetime.time)
    assert event_details["timezone"] in timezones

def test_task_func_with_invalid_timezone():
    epoch_milliseconds = 1672531200000  # Example epoch milliseconds for January 1, 2023
    timezones = ["Invalid/Timezone"]
    result = task_func(epoch_milliseconds, timezones=timezones)
    assert isinstance(result, dict)
    event_name = list(result.keys())[0]
    assert isinstance(event_name, str)
    event_details = result[event_name][0]
    assert isinstance(event_details, dict)
    assert isinstance(event_details["date"], datetime.date)
    assert isinstance(event_details["time"], datetime.time)
    assert event_details["timezone"] == "UTC"

def test_task_func_with_utc_offset_timezone():
    epoch_milliseconds = 1672531200000  # Example epoch milliseconds for January 1, 2023
    timezones = ["UTC+03:00"]
    result = task_func(epoch_milliseconds, timezones=timezones)
    assert isinstance(result, dict)
    event_name = list(result.keys())[0]
    assert isinstance(event_name, str)
    event_details = result[event_name][0]
    assert isinstance(event_details, dict)
    assert isinstance(event_details["date"], datetime.date)
    assert isinstance(event_details["time"], datetime.time)
    assert event_details["timezone"] == "UTC+03:00"