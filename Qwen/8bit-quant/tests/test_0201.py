import pytest
from src_0201 import task_func

def test_task_func_n_less_than_1():
    result = task_func(0, 0.5)
    assert result == ([], 0)

    result = task_func(-1, 0.5)
    assert result == ([], 0)

def test_task_func_positive_n():
    greater_avg, num_greater_value = task_func(10, 0.5)
    assert isinstance(greater_avg, list)
    assert isinstance(num_greater_value, int)
    assert 0 <= num_greater_value <= 10

def test_task_func_with_value_zero():
    greater_avg, num_greater_value = task_func(10, 0)
    assert isinstance(greater_avg, list)
    assert isinstance(num_greater_value, int)
    assert 0 <= num_greater_value <= 10

def test_task_func_with_value_one():
    greater_avg, num_greater_value = task_func(10, 1)
    assert isinstance(greater_avg, list)
    assert isinstance(num_greater_value, int)
    assert 0 <= num_greater_value <= 10

def test_task_func_with_large_n():
    greater_avg, num_greater_value = task_func(1000, 0.5)
    assert isinstance(greater_avg, list)
    assert isinstance(num_greater_value, int)
    assert 0 <= num_greater_value <= 1000

def test_task_func_with_small_n():
    greater_avg, num_greater_value = task_func(1, 0.5)
    assert isinstance(greater_avg, list)
    assert isinstance(num_greater_value, int)
    assert 0 <= num_greater_value <= 1