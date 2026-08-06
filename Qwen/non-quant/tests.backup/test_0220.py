import pytest
from src_0220 import task_func
import math
import statistics
import numpy as np

def test_task_func_with_empty_list():
    with pytest.raises(statistics.StatisticsError):
        task_func([])

def test_task_func_with_single_element():
    result = task_func([0])
    assert result == (0, 0, 0, 0, 0, 0)

def test_task_func_with_uniform_elements():
    result = task_func([1, 1, 1])
    assert result == (1, 1, 1, 0, 0, 0)

def test_task_func_with_distinct_elements():
    result = task_func([0, 90, 180, 270])
    assert result == (135, 90, 0, 1, 1, 1)

def test_task_func_with_negative_and_positive_angles():
    result = task_func([-90, 90, 180, -180])
    assert result == (45, 0, -180, 1, 1, 1)

def test_task_func_with_non_integer_angles():
    result = task_func([0.5, 90.5, 180.5, 270.5])
    assert result == (135.375, 90.5, 0.5, 1, 1, 1)

def test_task_func_with_large_angles():
    result = task_func([360, 720, 1080, 1440])
    assert result == (1080, 720, 360, 1, 1, 1)

def test_task_func_with_repeated_angles():
    result = task_func([45, 45, 45, 45])
    assert result == (45, 45, 45, 1, 1, 1)

def test_task_func_with_irregular_angles():
    result = task_func([10, 20, 30, 40, 50])
    assert result == (30, 30, 10, 1, 1, 1)