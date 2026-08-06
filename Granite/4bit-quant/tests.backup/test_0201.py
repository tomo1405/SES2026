import random
import bisect
import statistics
import matplotlib.pyplot as plt
from src_0201 import task_func
import pytest

def test_task_func():
    n = 10
    value = 0.5
    greater_avg, num_greater_value = task_func(n, value)
    assert len(greater_avg) == num_greater_value
    assert all(x > value for x in greater_avg)
    assert num_greater_value <= n

def test_task_func_with_zero_n():
    n = 0
    value = 0.5
    greater_avg, num_greater_value = task_func(n, value)
    assert greater_avg == []
    assert num_greater_value == 0

def test_task_func_with_negative_n():
    n = -1
    value = 0.5
    with pytest.raises(ValueError):
        task_func(n, value)

def test_task_func_with_negative_value():
    n = 10
    value = -1
    with pytest.raises(ValueError):
        task_func(n, value)