import pytest
from src_0313 import task_func

def test_task_func():
    distribution, _ = task_func()
    assert len(distribution) == 1000
    assert all(isinstance(x, float) for x in distribution)