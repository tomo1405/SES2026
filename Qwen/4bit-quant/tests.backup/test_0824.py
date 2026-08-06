import pytest
from src_0824 import task_func
import numpy as np

def test_task_func_default_values():
    mean, std = task_func()
    assert isinstance(mean, float)
    assert isinstance(std, float)
    assert mean > 0.1
    assert std > 0

def test_task_func_custom_samples():
    mean, std = task_func(samples=5)
    assert isinstance(mean, float)
    assert isinstance(std, float)
    assert mean > 0.1
    assert std > 0

def test_task_func_custom_delay():
    mean, std = task_func(delay=0.2)
    assert isinstance(mean, float)
    assert isinstance(std, float)
    assert mean > 0.2
    assert std > 0

def test_task_func_large_samples():
    mean, std = task_func(samples=100)
    assert isinstance(mean, float)
    assert isinstance(std, float)
    assert mean > 0.1
    assert std > 0

def test_task_func_zero_delay():
    mean, std = task_func(delay=0)
    assert isinstance(mean, float)
    assert isinstance(std, float)
    assert mean == 0
    assert std == 0

def test_task_func_negative_delay():
    with pytest.raises(ValueError):
        task_func(delay=-0.1)

def test_task_func_non_integer_samples():
    with pytest.raises(TypeError):
        task_func(samples=3.5)

def test_task_func_non_numeric_delay():
    with pytest.raises(TypeError):
        task_func(delay='a')