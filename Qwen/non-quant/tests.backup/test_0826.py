import pytest
from src_0826 import task_func
import numpy as np

def test_task_func_length():
    result = task_func(3)
    assert len(result) == 10
    assert all(len(item) == 3 for item in result)

def test_task_func_alphabets_default():
    result = task_func(2)
    assert all(all(char in string.ascii_lowercase for char in item) for item in result)

def test_task_func_alphabets_custom():
    custom_alphabets = ['a', 'b']
    result = task_func(2, alphabets=custom_alphabets)
    assert all(all(char in custom_alphabets for char in item) for item in result)

def test_task_func_seed():
    seed = 42
    result1 = task_func(2, seed=seed)
    result2 = task_func(2, seed=seed)
    assert result1 == result2

def test_task_func_empty_alphabets():
    with pytest.raises(ValueError):
        task_func(2, alphabets=[])

def test_task_func_negative_length():
    with pytest.raises(ValueError):
        task_func(-1)