import pytest
from src_0218 import task_func

def test_task_func():
    ax, mean, std = task_func()
    assert ax is not None
    assert isinstance(mean, float)
    assert isinstance(std, float)