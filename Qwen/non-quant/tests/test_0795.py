import string

import pytest
from src_0795 import task_func


def test_task_func_length():
    length = 10
    result = task_func(length)
    assert len(result) == length

def test_task_func_characters():
    length = 10
    result = task_func(length)
    valid_chars = string.ascii_lowercase + "(){}[]"
    assert all(char in valid_chars for char in result)

def test_task_func_random_seed():
    length = 10
    seed = 42
    result1 = task_func(length, random_seed=seed)
    result2 = task_func(length, random_seed=seed)
    assert result1 == result2

def test_task_func_no_seed():
    length = 10
    result1 = task_func(length)
    result2 = task_func(length)
    assert result1 != result2

def test_task_func_zero_length():
    length = 0
    result = task_func(length)
    assert result == ""

def test_task_func_negative_length():
    length = -5
    with pytest.raises(ValueError):
        task_func(length)