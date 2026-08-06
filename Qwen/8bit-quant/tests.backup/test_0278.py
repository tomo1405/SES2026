import pytest
from src_0278 import task_func

def test_task_func_with_n_less_than_2():
    assert task_func(1) is None
    assert task_func(0) is None
    assert task_func(-5) is None

def test_task_func_with_n_equal_to_2():
    result = task_func(2)
    assert len(result) == 2
    assert all(isinstance(point, tuple) and len(point) == 2 for point in result)

def test_task_func_with_n_greater_than_2():
    result = task_func(5)
    assert len(result) == 2
    assert all(isinstance(point, tuple) and len(point) == 2 for point in result)

def test_task_func_with_larger_n():
    result = task_func(10)
    assert len(result) == 2
    assert all(isinstance(point, tuple) and len(point) == 2 for point in result)

def test_task_func_consistency():
    result1 = task_func(3)
    result2 = task_func(3)
    assert result1 != result2  # Since points are randomly generated, results should be different

def test_task_func_with_large_n():
    result = task_func(100)
    assert len(result) == 2
    assert all(isinstance(point, tuple) and len(point) == 2 for point in result)