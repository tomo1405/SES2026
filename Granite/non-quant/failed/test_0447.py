import pytest
from src_0447 import task_func

def test_task_func():
    X, y, ax = task_func()
    assert X.shape == (100, 2)
    assert y.shape == (100,)
    assert ax.get_xlabel() == 'feature 0'
    assert ax.get_ylabel() == 'feature 1'