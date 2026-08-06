import pytest
from src_0824 import task_func
import numpy as np

def test_task_func():
    mean, std = task_func(samples=5, delay=0.1)
    assert isinstance(mean, float)
    assert isinstance(std, float)
    assert mean >= 0.1
    assert std > 0

def test_task_func_zero_samples():
    mean, std = task_func(samples=0, delay=0.1)
    assert mean == 0
    assert std == 0

def test_task_func_no_delay():
    mean, std = task_func(samples=5, delay=0)
    assert mean == 0
    assert std == 0

def test_task_func_large_samples():
    mean, std = task_func(samples=100, delay=0.1)
    assert isinstance(mean, float)
    assert isinstance(std, float)
    assert mean >= 0.1
    assert std > 0

def test_task_func_large_delay():
    mean, std = task_func(samples=5, delay=1)
    assert isinstance(mean, float)
    assert isinstance(std, float)
    assert mean >= 1
    assert std > 0