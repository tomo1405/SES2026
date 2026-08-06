import pytest
from src_0495 import task_func
from datetime import datetime
import pytz
import re
from faker import Faker

def test_task_func_with_default_parameters():
    epoch_milliseconds = 1633072800000  # Example epoch milliseconds for October 1, 2021
    result = task_func(epoch_milliseconds)
    
    assert isinstance(result, dict)
    event_name = list(result.keys())[0]
    assert isinstance(event_name, str)
    event_schedule = result[event_name]
    assert isinstance(event_schedule, list)
    assert len(event_schedule) == 1
    
    event_info = event_schedule[0]
    assert isinstance(event_info['date'], datetime.date)
    assert isinstance(event_info['time'], datetime.time)
    assert event_info['timezone'] == "UTC"

def test_task_func_with_custom_seed():
    epoch_milliseconds = 1633072800000
    seed = 42
    result = task_func(epoch_milliseconds, seed=seed)
    
    assert isinstance(result, dict)
    event_name = list(result.keys())[0]
    assert isinstance(event_name, str)
    event_schedule = result[event_name]
    assert isinstance(event_schedule, list)
    assert len(event_schedule) == 1
    
    event_info = event_schedule[0]
    assert isinstance(event_info['date'], datetime.date)
    assert isinstance(event_info['time'], datetime.time)
    assert event_info['timezone'] == "UTC"

def test_task_func_with_valid_timezone():
    epoch_milliseconds = 1633072800000
    timezones = ["UTC", "America/New_York"]
    result = task_func(epoch_milliseconds, timezones=timezones)
    
    assert isinstance(result, dict)
    event_name = list(result.keys())[0]
    assert isinstance(event_name, str)
    event_schedule = result[event_name]
    assert isinstance(event_schedule, list)
    assert len(event_schedule) == 1
    
    event_info = event_schedule[0]
    assert isinstance(event_info['date'], datetime.date)
    assert isinstance(event_info['time'], datetime.time)
    assert event_info['timezone'] in timezones

def test_task_func_with_invalid_timezone():
    epoch_milliseconds = 1633072800000
    timezones = ["Invalid/Timezone"]
    result = task_func(epoch_milliseconds, timezones=timezones)
    
    assert isinstance(result, dict)
    event_name = list(result.keys())[0]
    assert isinstance(event_name, str)
    event_schedule = result[event_name]
    assert isinstance(event_schedule, list)
    assert len(event_schedule) == 1
    
    event_info = event_schedule[0]
    assert isinstance(event_info['date'], datetime.date)
    assert isinstance(event_info['time'], datetime.time)
    assert event_info['timezone'] == "UTC"

def test_task_func_with_utc_offset():
    epoch_milliseconds = 1633072800000
    timezones = ["UTC+02:00"]
    result = task_func(epoch_milliseconds, timezones=timezones)
    
    assert isinstance(result, dict)
    event_name = list(result.keys())[0]
    assert isinstance(event_name, str)
    event_schedule = result[event_name]
    assert isinstance(event_schedule, list)
    assert len(event_schedule) == 1
    
    event_info = event_schedule[0]
    assert isinstance(event_info['date'], datetime.date)
    assert isinstance(event_info['time'], datetime.time)
    assert event_info['timezone'] == "UTC+02:00"