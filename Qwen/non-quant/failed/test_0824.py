import pytest
from src_0824 import task_func
import numpy as np

def test_task_func_default():
    mean, std = task_func()
    assert isinstance(mean, float)
    assert isinstance(std, float)
    assert mean > 0.1
    assert std > 0

def test_task_func_custom_samples():
    samples = 5
    mean, std = task_func(samples=samples)
    assert len(mean) == samples
    assert len(std) == samples
    assert mean > 0.1
    assert std > 0

def test_task_func_custom_delay():
    delay = 0.2
    mean, std = task_func(delay=delay)
    assert mean > delay
    assert std > 0

def test_task_func_no_samples():
    with pytest.raises(ValueError):
        task_func(samples=0)

def test_task_func_negative_delay():
    with pytest.raises(ValueError):
        task_func(delay=-0.1)