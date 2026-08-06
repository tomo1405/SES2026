import statistics

import pytest
from src_0011 import task_func


def test_task_func():
    T1 = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    mean, median, mode = task_func(T1)
    assert isinstance(mean, float)
    assert isinstance(median, float)
    assert isinstance(mode, float)

def test_task_func_with_empty_list():
    T1 = []
    with pytest.raises(statistics.StatisticsError):
        task_func(T1)

def test_task_func_with_non_numeric_values():
    T1 = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["a", "b", "c"]]
    with pytest.raises(ValueError):
        task_func(T1)