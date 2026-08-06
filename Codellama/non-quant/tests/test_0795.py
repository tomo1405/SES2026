import string

import pytest
from src_0795 import task_func


def test_task_func_length():
    length = 10
    result = task_func(length)
    assert len(result) == length

def test_task_func_random_seed():
    length = 10
    random_seed = 1234
    result1 = task_func(length, random_seed)
    result2 = task_func(length, random_seed)
    assert result1 == result2

def test_task_func_brackets():
    length = 10
    result = task_func(length)
    assert all(c in string.ascii_lowercase + "(){}[]" for c in result)

def test_task_func_invalid_length():
    length = 0
    with pytest.raises(ValueError):
        task_func(length)

def test_task_func_invalid_random_seed():
    length = 10
    random_seed = -1
    with pytest.raises(ValueError):
        task_func(length, random_seed)