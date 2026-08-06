import pytest
from src_0009 import task_func

def test_task_func():
    T1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    RANGE = 100
    expected_counts = Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1})
    assert task_func(T1, RANGE) == expected_counts

def test_task_func_with_different_range():
    T1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    RANGE = 50
    expected_counts = Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1})
    assert task_func(T1, RANGE) == expected_counts

def test_task_func_with_empty_list():
    T1 = []
    RANGE = 100
    expected_counts = Counter()
    assert task_func(T1, RANGE) == expected_counts

def test_task_func_with_invalid_input():
    T1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    RANGE = "invalid"
    with pytest.raises(ValueError):
        task_func(T1, RANGE)