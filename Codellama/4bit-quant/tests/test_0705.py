import pytest
from src_0705 import task_func

def test_task_func():
    data = [[1, 2], [3, 4], [5, 6]]
    cols = ['A', 'B']
    percentage = 0.75
    expected_result = [('A', 'B')]
    result = task_func(data, cols, percentage)
    assert result == expected_result

def test_task_func_invalid_percentage():
    data = [[1, 2], [3, 4], [5, 6]]
    cols = ['A', 'B']
    percentage = -0.1
    with pytest.raises(ValueError):
        task_func(data, cols, percentage)

def test_task_func_invalid_data():
    data = [[1, 2], [3, 4], [5, 6]]
    cols = ['A', 'B']
    percentage = 0.75
    with pytest.raises(ValueError):
        task_func(data, cols, percentage)