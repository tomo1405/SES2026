import pytest
from src_0059 import task_func

def test_task_func():
    fig = task_func(mu=0, sigma=1, num_samples=1000)
    assert fig is not None, "Expected a figure object to be returned"

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(mu='foo', sigma=1, num_samples=1000)
    with pytest.raises(ValueError):
        task_func(mu=0, sigma='bar', num_samples=1000)
    with pytest.raises(ValueError):
        task_func(mu=0, sigma=1, num_samples='baz')