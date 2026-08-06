import pytest
from src_0002 import task_func
import collections
import random
import string

def test_task_func_valid_input():
    result = task_func(length=100)
    assert isinstance(result, dict)
    assert all(isinstance(k, str) and isinstance(v, int) for k, v in result.items())

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(length=-1)

def test_task_func_random_input():
    for _ in range(100):
        length = random.randint(1, 1000)
        result = task_func(length=length)
        assert isinstance(result, dict)
        assert all(isinstance(k, str) and isinstance(v, int) for k, v in result.items())
        assert sum(result.values()) == length