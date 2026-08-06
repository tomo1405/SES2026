import pytest
from src_0705 import task_func

def test_task_func():
    data = [[1, 2], [3, 4], [5, 6]]
    cols = ['A', 'B']
    percentage = 0.75
    expected_result = [('A', 'B')]
    assert task_func(data, cols, percentage) == expected_result

def test_task_func_invalid_percentage():
    data = [[1, 2], [3, 4], [5, 6]]
    cols = ['A', 'B']
    percentage = 1.5
    with pytest.raises(ValueError):
        task_func(data, cols, percentage)

def test_task_func_empty_data():
    data = []
    cols = ['A', 'B']
    percentage = 0.75
    expected_result = []
    assert task_func(data, cols, percentage) == expected_result

def test_task_func_empty_cols():
    data = [[1, 2], [3, 4], [5, 6]]
    cols = []
    percentage = 0.75
    expected_result = []
    assert task_func(data, cols, percentage) == expected_result