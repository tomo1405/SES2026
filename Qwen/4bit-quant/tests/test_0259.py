import json
import random
from datetime import datetime

from src_0259 import task_func


def test_task_func_with_fixed_seed():
    # Test with a fixed seed to ensure reproducibility
    utc_datetime = datetime(2023, 10, 1, 12, 0, 0)
    expected_person = {
        'name': 'John',
        'age': 30,
        'city': 'New York',
        'timestamp': '2023-10-01T12:00:00'
    }
    expected_json_str = json.dumps(expected_person)
    
    result = task_func(utc_datetime, seed=0)
    assert result == expected_json_str

def test_task_func_with_random_seed():
    # Test with a random seed to check if the function handles it correctly
    utc_datetime = datetime(2023, 10, 1, 12, 0, 0)
    random.seed(None)  # Use system time as seed for randomness
    result = task_func(utc_datetime)
    
    # Parse the JSON string to a dictionary
    result_dict = json.loads(result)
    
    # Check if 'timestamp' is present and matches the input datetime
    assert 'timestamp' in result_dict
    assert result_dict['timestamp'] == utc_datetime.isoformat()
    
    # Check if the person data is one of the entries in DATA
    assert result_dict in DATA

def test_task_func_with_different_datetime():
    # Test with a different datetime
    utc_datetime = datetime(2023, 10, 2, 13, 30, 0)
    expected_timestamp = '2023-10-02T13:30:00'
    
    result = task_func(utc_datetime, seed=0)
    result_dict = json.loads(result)
    
    assert result_dict['timestamp'] == expected_timestamp