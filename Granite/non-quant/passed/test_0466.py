import json
from datetime import datetime
import numpy as np
from decimal import Decimal
from src_0466 import task_func

def test_task_func_with_int():
    my_obj = 123
    expected_result = '123'
    result = task_func(my_obj)
    assert result == expected_result

def test_task_func_with_list():
    my_obj = [1, 2, 3]
    expected_result = '[1, 2, 3]'
    result = task_func(my_obj)
    assert result == expected_result

def test_task_func_with_dict():
    my_obj = {'a': 1, 'b': 2}
    expected_result = '{"a": 1, "b": 2}'
    result = task_func(my_obj)
    assert result == expected_result

def test_task_func_with_datetime():
    my_obj = datetime(2023, 5, 1)
    expected_result = '"2023-05-01T00:00:00"'
    result = task_func(my_obj)
    assert result == expected_result

def test_task_func_with_numpy_array():
    my_obj = np.array([1, 2, 3])
    expected_result = '[1, 2, 3]'
    result = task_func(my_obj)
    assert result == expected_result

def test_task_func_with_decimal():
    my_obj = Decimal('1.23')
    expected_result = '"1.23"'
    result = task_func(my_obj)
    assert result == expected_result