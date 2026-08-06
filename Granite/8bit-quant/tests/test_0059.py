import pytest
from src_0059 import task_func

def test_task_func():
    fig = task_func(mu=0, sigma=1, num_samples=1000)
    assert fig is not None