import pytest
from src_0705 import task_func

def test_task_func_valid_input():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    cols = ['A', 'B', 'C']
    percentage = 0.75
    result = task_func(data, cols, percentage)
    assert isinstance(result, list)
    assert all(isinstance(item, tuple) and len(item) == 2 for item in result)

def test_task_func_no_correlations():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    cols = ['A', 'B', 'C']
    percentage = 1.0
    result = task_func(data, cols, percentage)
    assert result == []

def test_task_func_all_correlations():
    data = [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    cols = ['A', 'B', 'C']
    percentage = 0.0
    result = task_func(data, cols, percentage)
    assert set(result) == {('A', 'B'), ('A', 'C'), ('B', 'C')}

def test_task_func_invalid_percentage():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    cols = ['A', 'B', 'C']
    percentage = 1.5
    with pytest.raises(ValueError):
        task_func(data, cols, percentage)

def test_task_func_empty_data():
    data = []
    cols = ['A', 'B', 'C']
    percentage = 0.75
    result = task_func(data, cols, percentage)
    assert result == []

def test_task_func_single_column():
    data = [[1], [2], [3]]
    cols = ['A']
    percentage = 0.75
    result = task_func(data, cols, percentage)
    assert result == []

def test_task_func_min_percentage_constant():
    assert MIN_PERCENTAGE == 0.75