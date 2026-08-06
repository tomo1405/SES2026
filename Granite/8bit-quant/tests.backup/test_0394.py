import pytest
from src_0394 import task_func

def test_task_func():
    fig = task_func(mu=0, sigma=1)
    assert fig is not None
    assert fig.get_size_inches() == (12, 6)