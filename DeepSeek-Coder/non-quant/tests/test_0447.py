import pytest
from src_0447 import task_func

def test_task_func():
    X, y, ax = task_func()
    assert X.shape == (100, 2)
    assert y.shape == (100,)
    assert ax is not None