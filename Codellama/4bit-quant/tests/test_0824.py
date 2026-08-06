import pytest
from src_0824 import task_func

def test_task_func():
    samples = 10
    delay = 0.1
    mean, std = task_func(samples, delay)
    assert mean == delay
    assert std == 0

def test_task_func_with_different_samples():
    samples = 20
    delay = 0.1
    mean, std = task_func(samples, delay)
    assert mean == delay
    assert std == 0

def test_task_func_with_different_delay():
    samples = 10
    delay = 0.2
    mean, std = task_func(samples, delay)
    assert mean == delay
    assert std == 0