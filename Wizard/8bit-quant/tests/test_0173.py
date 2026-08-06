python
import json
from datetime import datetime
import pytest

def task_func(json_data):
    try:
        # Convert JSON string to Python dictionary
        data = json.loads(json_data)

        # Extract datetime string from dictionary
        datetime_str = data['utc_datetime']

        # Convert datetime string to datetime object
        utc_datetime = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S')

        # Check if the day of the week is Saturday (5) or Sunday (6)
        return utc_datetime.weekday() >= 5
    except Exception as e:
        raise e

def test_task_func_valid_json():
    # Test with valid JSON string
    json_data = '{"utc_datetime": "2022-01-01T00:00:00"}'
    assert task_func(json_data) == False

def test_task_func_invalid_json():
    # Test with invalid JSON string
    json_data = '{"utc_datetime": "2022-01-01T00:00:00"'
    with pytest.raises(json.JSONDecodeError):
        task_func(json_data)

def test_task_func_saturday():
    # Test with Saturday datetime
    json_data = '{"utc_datetime": "2022-01-05T00:00:00"}'
    assert task_func(json_data) == True

def test_task_func_sunday():
    # Test with Sunday datetime
    json_data = '{"utc_datetime": "2022-01-06T00:00:00"}'
    assert task_func(json_data) == True

def test_task_func_weekday():
    # Test with weekday datetime
    json_data = '{"utc_datetime": "2022-01-02T00:00:00"}'
    assert task_func(json_data) == False