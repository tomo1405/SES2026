import pytest
from src_0824 import task_func

def test_task_func():
    mean, std = task_func()
    assert isinstance(mean, float)
    assert isinstance(std, float)
    assert mean >= 0
    assert std >= 0

def test_task_func_with_samples():
    samples = 100
    mean, std = task_func(samples=samples)
    assert isinstance(mean, float)
    assert isinstance(std, float)
    assert mean >= 0
    assert std >= 0
    assert samples == len(task_func(samples=samples)[0])

def test_task_func_with_delay():
    delay = 0.5
    mean, std = task_func(delay=delay)
    assert isinstance(mean, float)
    assert isinstance(std, float)
    assert mean >= 0
    assert std >= 0
    assert delay == task_func(delay=delay)[0][0]