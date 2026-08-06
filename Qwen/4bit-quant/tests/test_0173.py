import json

import pytest
from src_0173 import task_func


def test_task_func_valid_saturday():
    json_data = '{"utc_datetime": "2023-10-07T12:00:00"}'  # Saturday
    assert task_func(json_data) == True

def test_task_func_valid_sunday():
    json_data = '{"utc_datetime": "2023-10-08T12:00:00"}'  # Sunday
    assert task_func(json_data) == True

def test_task_func_valid_weekday():
    json_data = '{"utc_datetime": "2023-10-09T12:00:00"}'  # Monday
    assert task_func(json_data) == False

def test_task_func_invalid_json_format():
    json_data = '{"utc_datetime": "2023-10-09T12:00:00"'  # Missing closing brace
    with pytest.raises(json.JSONDecodeError):
        task_func(json_data)

def test_task_func_missing_key():
    json_data = '{"datetime": "2023-10-09T12:00:00"}'  # Missing 'utc_datetime' key
    with pytest.raises(KeyError):
        task_func(json_data)

def test_task_func_invalid_datetime_format():
    json_data = '{"utc_datetime": "2023-10-09 12:00:00"}'  # Incorrect format
    with pytest.raises(ValueError):
        task_func(json_data)