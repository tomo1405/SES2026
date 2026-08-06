import pytest
from src_0011 import task_func

def test_task_func():
    T1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    RANGE = 100
    mean, median, mode = task_func(T1, RANGE)
    assert mean == 5
    assert median == 5
    assert mode == 5

def test_task_func_empty_list():
    T1 = []
    RANGE = 100
    with pytest.raises(statistics.StatisticsError):
        task_func(T1, RANGE)

def test_task_func_invalid_range():
    T1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    RANGE = 0
    with pytest.raises(ValueError):
        task_func(T1, RANGE)

def test_task_func_invalid_input():
    T1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    RANGE = 100
    with pytest.raises(TypeError):
        task_func(T1, "invalid_range")