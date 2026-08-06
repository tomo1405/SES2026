import pytest
from src_0466 import task_func
import json
from datetime import datetime
import numpy as np
from decimal import Decimal

def test_task_func_with_datetime():
    my_obj = {"timestamp": datetime(2023, 10, 1, 12, 30, 45)}
    expected_output = '{"timestamp": "2023-10-01T12:30:45"}'
    assert task_func(my_obj) == expected_output

def test_task_func_with_numpy_array():
    my_obj = {"array": np.array([1, 2, 3])}
    expected_output = '{"array": [1, 2, 3]}'
    assert task_func(my_obj) == expected_output

def test_task_func_with_decimal():
    my_obj = {"decimal_value": Decimal('123.456')}
    expected_output = '{"decimal_value": "123.456"}'
    assert task_func(my_obj) == expected_output

def test_task_func_with_mixed_types():
    my_obj = {
        "timestamp": datetime(2023, 10, 1, 12, 30, 45),
        "array": np.array([1, 2, 3]),
        "decimal_value": Decimal('123.456'),
        "simple_value": 42
    }
    expected_output = '{"timestamp": "2023-10-01T12:30:45", "array": [1, 2, 3], "decimal_value": "123.456", "simple_value": 42}'
    assert task_func(my_obj) == expected_output

def test_task_func_with_simple_dict():
    my_obj = {"key": "value"}
    expected_output = '{"key": "value"}'
    assert task_func(my_obj) == expected_output

def test_task_func_with_empty_dict():
    my_obj = {}
    expected_output = '{}'
    assert task_func(my_obj) == expected_output