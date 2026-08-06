import pytest
from src_0705 import task_func

def test_task_func_valid_input():
    data = [[1, 2], [3, 4]]
    cols = ['a', 'b']
    percentage = 0.75
    expected_output = [('a', 'b')]
    assert task_func(data, cols, percentage) == expected_output

def test_task_func_invalid_input():
    data = [[1, 2], [3, 4]]
    cols = ['a', 'b']
    percentage = 1.5
    with pytest.raises(ValueError):
        task_func(data, cols, percentage)