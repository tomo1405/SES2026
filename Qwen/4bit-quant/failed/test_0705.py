import pytest
from src_0705 import task_func

def test_task_func_valid_data():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    cols = ['A', 'B', 'C']
    percentage = 0.75
    result = task_func(data, cols, percentage)
    assert result == []

def test_task_func_with_high_correlation():
    data = [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    cols = ['A', 'B', 'C']
    percentage = 0.75
    result = task_func(data, cols, percentage)
    assert result == [('A', 'B'), ('A', 'C'), ('B', 'C')]

def test_task_func_with_no_correlation():
    data = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    cols = ['A', 'B', 'C']
    percentage = 0.75
    result = task_func(data, cols, percentage)
    assert result == []

def test_task_func_with_low_percentage():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    cols = ['A', 'B', 'C']
    percentage = 0.1
    result = task_func(data, cols, percentage)
    assert result == [('A', 'B'), ('A', 'C'), ('B', 'C')]

def test_task_func_invalid_percentage():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    cols = ['A', 'B', 'C']
    percentage = 1.5
    with pytest.raises(ValueError) as excinfo:
        task_func(data, cols, percentage)
    assert str(excinfo.value) == 'Percentage must be between 0 and 1'

def test_task_func_empty_data():
    data = []
    cols = ['A', 'B', 'C']
    percentage = 0.75
    result = task_func(data, cols, percentage)
    assert result == []

def test_task_func_single_row_data():
    data = [[1, 2, 3]]
    cols = ['A', 'B', 'C']
    percentage = 0.75
    result = task_func(data, cols, percentage)
    assert result == []