import pytest
from src_0360 import task_func

def test_task_func():
    data_dict = {'x': [1, 2, 3, 4, 5], 'y': [2, 4, 6, 8, 10]}
    data_keys = ['x', 'y']
    correlation, ax = task_func(data_dict, data_keys)
    assert correlation == 1.0
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'
    assert ax.get_title() == 'Correlation between x and y'