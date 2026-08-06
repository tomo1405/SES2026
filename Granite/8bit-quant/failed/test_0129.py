import pytest
from src_0129 import task_func

def test_task_func():
    fig = task_func()
    assert fig is not None
    assert fig.get_size_inches() == (6.4, 4.8)