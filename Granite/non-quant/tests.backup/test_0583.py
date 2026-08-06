import pytest
from src_0583 import task_func

def test_task_func():
    # Test case 1: Default size
    fig = task_func()
    assert fig is not None
    assert fig.get_size_inches() == (6, 4)

    # Test case 2: Custom size
    fig = task_func(size=2000)
    assert fig is not None
    assert fig.get_size_inches() == (12, 8)