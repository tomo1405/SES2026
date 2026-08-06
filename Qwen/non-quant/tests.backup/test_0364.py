import pytest
from src_0364 import task_func

def test_task_func_single_number():
    result = task_func([5])
    assert result == {5: 120}

def test_task_func_multiple_numbers():
    result = task_func([0, 1, 2, 3, 4])
    assert result == {0: 1, 1: 1, 2: 2, 3: 6, 4: 24}

def test_task_func_large_number():
    result = task_func([10])
    assert result == {10: 3628800}

def test_task_func_empty_list():
    result = task_func([])
    assert result == {}

def test_task_func_negative_number():
    with pytest.raises(ValueError):
        task_func([-1])

def test_task_func_non_integer():
    with pytest.raises(ValueError):
        task_func([1.5, 2])

def test_task_func_mixed_types():
    with pytest.raises(ValueError):
        task_func([1, 'a', 3])

def test_task_func_large_list():
    numbers = list(range(10))
    expected = {i: math.factorial(i) for i in numbers}
    result = task_func(numbers)
    assert result == expected