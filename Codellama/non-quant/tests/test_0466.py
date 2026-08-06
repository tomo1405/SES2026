from datetime import datetime

import numpy as np
from src_0466 import task_func


def test_task_func_datetime():
    my_obj = {'a': datetime.now()}
    result = task_func(my_obj)
    assert result == '{"a": "2023-02-21T15:16:23.456789"}'

def test_task_func_numpy_array():
    my_obj = {'a': np.array([1, 2, 3])}
    result = task_func(my_obj)
    assert result == '{"a": [1, 2, 3]}'

def test_task_func_decimal():
    my_obj = {'a': Decimal('1.23')}
    result = task_func(my_obj)
    assert result == '{"a": "1.23"}'

def test_task_func_default():
    my_obj = {'a': 'test'}
    result = task_func(my_obj)
    assert result == '{"a": "test"}'