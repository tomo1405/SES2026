import pytest
from src_0823 import task_func

def test_task_func_length_zero():
    with pytest.raises(ValueError, match="Length must be a positive integer."):
        task_func(0, 1)

def test_task_func_negative_length():
    with pytest.raises(ValueError, match="Length must be a positive integer."):
        task_func(-5, 2)

def test_task_func_num_digits_negative():
    with pytest.raises(ValueError, match="num_digits must be a non-negative integer and less than or equal to length."):
        task_func(5, -1)

def test_task_func_num_digits_greater_than_length():
    with pytest.raises(ValueError, match="num_digits must be a non-negative integer and less than or equal to length."):
        task_func(5, 6)

def test_task_func_no_digits():
    result = task_func(5, 0)
    assert len(result) == 5
    assert all(char in string.ascii_letters for char in result)

def test_task_func_all_digits():
    result = task_func(5, 5)
    assert len(result) == 5
    assert all(char in string.digits for char in result)

def test_task_func_mixed_characters():
    result = task_func(5, 2)
    assert len(result) == 5
    assert sum(char in string.digits for char in result) == 2
    assert sum(char in string.ascii_letters for char in result) == 3

def test_task_func_reproducibility():
    result1 = task_func(5, 2)
    result2 = task_func(5, 2)
    assert result1 == result2