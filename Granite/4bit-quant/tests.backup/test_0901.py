import pandas as pd
import numpy as np
from src_0901 import task_func

def test_task_func_valid_input():
    input_data = [
        {'x': 1, 'y': 2, 'z': 3},
        {'x': 4, 'y': 5, 'z': 6},
        {'x': 7, 'y': 8, 'z': 9}
    ]
    expected_output = {
        'x': {'mean': 5.0, 'sum': 15, 'max': 7, 'min': 4, 'std': 2.160246899469287},
        'y': {'mean': 6.0, 'sum': 18, 'max': 8, 'min': 5, 'std': 2.160246899469287},
        'z': {'mean': 7.0, 'sum': 21, 'max': 9, 'min': 6, 'std': 2.160246899469287}
    }
    assert task_func(input_data) == expected_output

def test_task_func_invalid_input():
    input_data = [
        {'x': 1, 'y': 2, 'z': 3},
        {'x': 4, 'y': 5, 'z': 6},
        7
    ]
    with pytest.raises(ValueError) as exc_info:
        task_func(input_data)
    assert str(exc_info.value) == "Input must be a list of dictionaries."

def test_task_func_empty_input():
    input_data = []
    expected_output = {
        'x': None,
        'y': None,
        'z': None
    }
    assert task_func(input_data) == expected_output