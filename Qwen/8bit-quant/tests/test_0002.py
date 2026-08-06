import string

import pytest
from src_0002 import task_func


def test_task_func_length():
    result = task_func(10)
    assert len(result) <= 10

def test_task_func_negative_length():
    with pytest.raises(ValueError):
        task_func(-1)

def test_task_func_default_length():
    result = task_func()
    assert len(result) <= 100

def test_task_func_character_types():
    result = task_func(10)
    for char in result.keys():
        assert char in string.ascii_letters

def test_task_func_counter_values():
    result = task_func(10)
    for count in result.values():
        assert isinstance(count, int) and count > 0

def test_task_func_randomness():
    result1 = task_func(10)
    result2 = task_func(10)
    assert result1 != result2