import pytest
from src_0466 import task_func
from datetime import datetime
import numpy as np
from decimal import Decimal

def test_task_func_with_datetime():
    my_obj = {"timestamp": datetime(2023, 1, 1)}
    expected_output = '{"timestamp": "2023-01-01T00:00:00"}'
    assert task_func(my_obj) == expected_output

def test_task_func_with_numpy_array():
    my_obj = {"array": np.array([1, 2, 3])}
    expected_output = '{"array": [1, 2, 3]}'
    assert task_func(my_obj) == expected_output

def test_task_func_with_decimal():
    my_obj = {"decimal_value": Decimal('123.45')}
    expected_output = '{"decimal_value": "123.45"}'
    assert task_func(my_obj) == expected_output

def test_task_func_with_complex_object():
    my_obj = {
        "timestamp": datetime(2023, 1, 1),
        "array": np.array([1, 2, 3]),
        "decimal_value": Decimal('123.45')
    }
    expected_output = '{"timestamp": "2023-01-01T00:00:00", "array": [1, 2, 3], "decimal_value": "123.45"}'
    assert task_func(my_obj) == expected_output

def test_task_func_with_simple_dict():
    my_obj = {"key": "value"}
    expected_output = '{"key": "value"}'
    assert task_func(my_obj) == expected_output

def test_task_func_with_empty_dict():
    my_obj = {}
    expected_output = '{}'
    assert task_func(my_obj) == expected_output