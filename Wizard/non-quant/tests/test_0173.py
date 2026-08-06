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

def test_task_func():
    # Test case 1: Valid JSON string with Saturday date
    json_data = '{"utc_datetime": "2022-05-25T12:30:00"}'
    assert task_func(json_data) == True

    # Test case 2: Valid JSON string with Sunday date
    json_data = '{"utc_datetime": "2022-05-26T12:30:00"}'
    assert task_func(json_data) == True

    # Test case 3: Invalid JSON string
    json_data = '{"utc_datetime": "2022-05-25T12:30:00"'
    with pytest.raises(json.JSONDecodeError):
        task_func(json_data)

    # Test case 4: JSON string with missing key
    json_data = '{"datetime": "2022-05-25T12:30:00"}'
    with pytest.raises(KeyError):
        task_func(json_data)

    # Test case 5: JSON string with invalid datetime format
    json_data = '{"utc_datetime": "2022-05-25T12:30:00Z"}'
    with pytest.raises(ValueError):
        task_func(json_data)