import pytest
from src_0364 import task_func

def test_task_func_with_single_number():
    result = task_func([5])
    assert result == {5: 120}

def test_task_func_with_multiple_numbers():
    result = task_func([0, 1, 2, 3, 4])
    assert result == {0: 1, 1: 1, 2: 2, 3: 6, 4: 24}

def test_task_func_with_large_numbers():
    result = task_func([10, 20])
    assert result == {10: 3628800, 20: 2432902008176640000}

def test_task_func_with_empty_list():
    result = task_func([])
    assert result == {}

def test_task_func_with_negative_numbers():
    with pytest.raises(ValueError):
        task_func([-1, 2, 3])

def test_task_func_with_non_integer_elements():
    with pytest.raises(ValueError):
        task_func([1, 'a', 3])

def test_task_func_with_mixed_types():
    with pytest.raises(ValueError):
        task_func([1, 2.5, 3])