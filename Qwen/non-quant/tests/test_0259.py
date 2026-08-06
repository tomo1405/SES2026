import json
from datetime import datetime, timezone

import pytest
from src_0259 import task_func


@pytest.mark.parametrize("seed", [0, 1, 42])
def test_task_func(seed):
    # Use a fixed UTC datetime for consistency
    utc_datetime = datetime(2023, 10, 1, 12, 0, 0, tzinfo=timezone.utc)
    
    # Call the function with the fixed datetime and seed
    result = task_func(utc_datetime, seed)
    
    # Decode the JSON string back to a dictionary
    person_dict = json.loads(result)
    
    # Check that the timestamp is correct
    assert person_dict['timestamp'] == utc_datetime.isoformat()
    
    # Check that the person data is one of the entries in DATA
    assert person_dict in DATA

def test_task_func_randomness():
    # Use a fixed UTC datetime for consistency
    utc_datetime = datetime(2023, 10, 1, 12, 0, 0, tzinfo=timezone.utc)
    
    # Call the function with different seeds
    result1 = task_func(utc_datetime, seed=0)
    result2 = task_func(utc_datetime, seed=1)
    
    # Decode the JSON strings back to dictionaries
    person_dict1 = json.loads(result1)
    person_dict2 = json.loads(result2)
    
    # Check that the results are different when seeds are different
    assert person_dict1 != person_dict2