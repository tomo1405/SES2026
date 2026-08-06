import pytest
from src_0276 import task_func

def test_task_func_positive_integer():
    result = task_func(3)
    expected = [(1, 2), (1, 3), (2, 3)]
    assert result == expected

def test_task_func_single_element():
    result = task_func(1)
    expected = []
    assert result == expected

def test_task_func_large_number():
    result = task_func(5)
    expected = [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
    assert result == expected

def test_task_func_zero_input():
    with pytest.raises(ValueError):
        task_func(0)

def test_task_func_negative_input():
    with pytest.raises(ValueError):
        task_func(-1)

def test_task_func_non_integer_input():
    with pytest.raises(TypeError):
        task_func(3.5)