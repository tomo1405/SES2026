python
import json
import math
import pytest

def task_func(decimal_value, precision=2):
    # Calculate the square root of the decimal value
    square_root = round(math.sqrt(decimal_value), precision)
    
    # Encode the result as a JSON string
    json_str = json.dumps(str(square_root))
    
    return json_str

def test_task_func():
    # Test case 1: decimal_value = 16, precision = 2
    assert task_func(16, 2) == '4.0'
    
    # Test case 2: decimal_value = 25, precision = 3
    assert task_func(25, 3) == '5.000'
    
    # Test case 3: decimal_value = 36, precision = 4
    assert task_func(36, 4) == '6.0000'