import pytest
from src_0824 import task_func

def test_task_func():
    result = task_func()
    assert isinstance(result, tuple), "The function should return a tuple."
    mean, std = result
    assert isinstance(mean, (int, float)), "The mean should be a number."
    assert isinstance(std, (int, float)), "The standard deviation should be a number."
    assert mean >= 0, "The mean should be non-negative."
    assert std >= 0, "The standard deviation should be non-negative."