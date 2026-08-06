import pytest
from src_0199 import task_func
import numpy as np

def test_task_func_empty_data():
    data = []
    value = 0
    expected_greater_avg = np.array([])
    expected_num_greater_value = 0

    greater_avg, num_greater_value = task_func(data, value)

    assert np.array_equal(greater_avg, expected_greater_avg)
    assert num_greater_value == expected_num_greater_value

def test_task_func_non_empty_data():
    data = [1, 2, 3, 4, 5]
    value = 3
    expected_greater_avg = np.array([4, 5])
    expected_num_greater_value = 2

    greater_avg, num_greater_value = task_func(data, value)

    assert np.array_equal(greater_avg, expected_greater_avg)
    assert num_greater_value == expected_num_greater_value