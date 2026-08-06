import pytest
from src_0823 import task_func

def test_task_func_length_zero():
    with pytest.raises(ValueError, match="Length must be a positive integer."):
        task_func(0, 0)

def test_task_func_negative_length():
    with pytest.raises(ValueError, match="Length must be a positive integer."):
        task_func(-1, 0)

def test_task_func_num_digits_greater_than_length():
    with pytest.raises(ValueError, match="num_digits must be a non-negative integer and less than or equal to length."):
        task_func(5, 6)

def test_task_func_num_digits_negative():
    with pytest.raises(ValueError, match="num_digits must be a non-negative integer and less than or equal to length."):
        task_func(5, -1)

def test_task_func_no_digits():
    assert task_func(5, 0) == 'bLxXq'

def test_task_func_all_digits():
    assert task_func(5, 5) == '53918'

def test_task_func_mixed():
    assert task_func(5, 2) == 'a7B3k'

def test_task_func_reproducibility():
    assert task_func(5, 2) == task_func(5, 2)