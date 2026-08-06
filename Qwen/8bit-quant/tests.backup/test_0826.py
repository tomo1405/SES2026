import pytest
from src_0826 import task_func
import numpy as np

def test_task_func_length():
    result = task_func(2)
    assert len(result) == 10
    for item in result:
        assert len(item) == 2

def test_task_func_alphabets():
    result = task_func(1)
    assert all(item in string.ascii_lowercase for item in result)

def test_task_func_seed():
    result1 = task_func(2, seed=42)
    result2 = task_func(2, seed=42)
    assert result1 == result2

def test_task_func_custom_alphabets():
    custom_alphabets = ['a', 'b']
    result = task_func(2, alphabets=custom_alphabets)
    assert all(item in ['aa', 'ab', 'ba', 'bb'] for item in result)

def test_task_func_large_length():
    result = task_func(3)
    assert len(result) == 10
    for item in result:
        assert len(item) == 3

def test_task_func_empty_alphabets():
    with pytest.raises(ValueError):
        task_func(1, alphabets=[])

def test_task_func_negative_length():
    with pytest.raises(ValueError):
        task_func(-1)