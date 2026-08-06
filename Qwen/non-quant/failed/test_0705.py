import pytest
from src_0705 import task_func

def test_task_func_valid_data():
    data = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    cols = ['A', 'B', 'C']
    percentage = 0.75
    result = task_func(data, cols, percentage)
    assert isinstance(result, list)
    assert all(isinstance(item, tuple) for item in result)
    assert all(len(item) == 2 for item in result)

def test_task_func_no_correlation():
    data = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    cols = ['A', 'B', 'C']
    percentage = 0.99
    result = task_func(data, cols, percentage)
    assert result == []

def test_task_func_all_correlation():
    data = [
        [1, 1, 1],
        [2, 2, 2],
        [3, 3, 3]
    ]
    cols = ['A', 'B', 'C']
    percentage = 0.5
    result = task_func(data, cols, percentage)
    assert set(result) == {('A', 'B'), ('A', 'C'), ('B', 'C')}

def test_task_func_invalid_percentage():
    data = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
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

def test_task_func_single_row():
    data = [
        [1, 2, 3]
    ]
    cols = ['A', 'B', 'C']
    percentage = 0.75
    result = task_func(data, cols, percentage)
    assert result == []