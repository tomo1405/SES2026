import pytest
from src_0173 import task_func
import json
from datetime import datetime

def test_task_func_weekend():
    # Test case where the datetime string corresponds to a weekend
    json_data = '{"utc_datetime": "2023-10-07T12:00:00"}'
    result = task_func(json_data)
    assert result is True

def test_task_func_weekday():
    # Test case where the datetime string corresponds to a weekday
    json_data = '{"utc_datetime": "2023-10-06T12:00:00"}'
    result = task_func(json_data)
    assert result is False

def test_task_func_invalid_json():
    # Test case with invalid JSON data
    json_data = 'invalid_json'
    with pytest.raises(Exception):
        task_func(json_data)