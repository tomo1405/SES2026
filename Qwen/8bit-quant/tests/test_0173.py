import json

import pytest
from src_0173 import task_func


def test_task_func_saturday():
    # Test with a Saturday date
    json_data = '{"utc_datetime": "2023-10-07T12:00:00"}'
    assert task_func(json_data) == True

def test_task_func_sunday():
    # Test with a Sunday date
    json_data = '{"utc_datetime": "2023-10-08T12:00:00"}'
    assert task_func(json_data) == True

def test_task_func_weekday():
    # Test with a weekday date
    json_data = '{"utc_datetime": "2023-10-09T12:00:00"}'
    assert task_func(json_data) == False

def test_task_func_invalid_json():
    # Test with invalid JSON
    json_data = '{"utc_datetime": "2023-10-09T12:00:00"'
    with pytest.raises(json.JSONDecodeError):
        task_func(json_data)

def test_task_func_missing_key():
    # Test with missing 'utc_datetime' key
    json_data = '{"some_other_key": "2023-10-09T12:00:00"}'
    with pytest.raises(KeyError):
        task_func(json_data)

def test_task_func_invalid_datetime_format():
    # Test with invalid datetime format
    json_data = '{"utc_datetime": "2023-10-09 12:00:00"}'
    with pytest.raises(ValueError):
        task_func(json_data)