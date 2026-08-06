import pytest
from src_0364 import task_func

def test_task_func_with_positive_numbers():
    assert task_func([0, 1, 2, 3, 4]) == {0: 1, 1: 1, 2: 2, 3: 6, 4: 24}

def test_task_func_with_single_number():
    assert task_func([5]) == {5: 120}

def test_task_func_with_empty_list():
    assert task_func([]) == {}

def test_task_func_with_large_numbers():
    assert task_func([10, 20]) == {10: 3628800, 20: 2432902008176640000}

def test_task_func_with_invalid_input():
    with pytest.raises(ValueError):
        task_func([1, -2, 3])

def test_task_func_with_non_integer_input():
    with pytest.raises(ValueError):
        task_func([1, 'a', 3])