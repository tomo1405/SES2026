import pytest
from src_0257 import task_func
from datetime import datetime
import json
import hashlib

def test_task_func_with_valid_inputs():
    # Define valid inputs
    utc_datetime = datetime(2023, 10, 1, 12, 0, 0)
    salt = 'pepper'
    password_length = 12
    seed = 42
    
    # Expected output
    expected_output = task_func(utc_datetime, salt, password_length, seed)
    
    # Actual output
    actual_output = task_func(utc_datetime, salt, password_length, seed)
    
    # Check if the output is a valid JSON string
    assert json.loads(actual_output) == json.loads(expected_output)

def test_task_func_invalid_utc_datetime():
    with pytest.raises(ValueError, match="Input should be a datetime object"):
        task_func("2023-10-01 12:00:00", salt='pepper')

def test_task_func_invalid_salt():
    utc_datetime = datetime(2023, 10, 1, 12, 0, 0)
    with pytest.raises(ValueError, match="Salt should be a string"):
        task_func(utc_datetime, salt=12345)

def test_task_func_with_default_values():
    utc_datetime = datetime(2023, 10, 1, 12, 0, 0)
    expected_output = task_func(utc_datetime)
    
    # Actual output
    actual_output = task_func(utc_datetime)
    
    # Check if the output is a valid JSON string
    assert json.loads(actual_output) == json.loads(expected_output)

def test_task_func_with_different_seed():
    utc_datetime = datetime(2023, 10, 1, 12, 0, 0)
    salt = 'pepper'
    password_length = 12
    
    # Different seeds should produce different results
    output1 = task_func(utc_datetime, salt, password_length, seed=1)
    output2 = task_func(utc_datetime, salt, password_length, seed=2)
    
    assert output1 != output2