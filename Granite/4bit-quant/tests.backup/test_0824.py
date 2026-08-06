import pytest
from src_0824 import task_func

def test_task_func():
    mean, std = task_func()
    assert isinstance(mean, float)
    assert isinstance(std, float)
    assert mean >= 0
    assert std >= 0

def test_task_func_with_samples():
    mean, std = task_func(samples=100)
    assert isinstance(mean, float)
    assert isinstance(std, float)
    assert mean >= 0
    assert std >= 0

def test_task_func_with_delay():
    mean, std = task_func(delay=0.5)
    assert isinstance(mean, float)
    assert isinstance(std, float)
    assert mean >= 0
    assert std >= 0