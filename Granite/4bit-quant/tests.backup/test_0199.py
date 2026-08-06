import pytest
from src_0199 import task_func

def test_task_func():
    data = [1, 2, 3, 4, 5]
    value = 3
    expected_output = (np.array([4, 5]), 2)
    output = task_func(data, value)
    assert output == expected_output, "Output does not match expected output"

def test_task_func_empty_data():
    data = []
    value = 3
    expected_output = (np.array([]), 0)
    output = task_func(data, value)
    assert output == expected_output, "Output does not match expected output"