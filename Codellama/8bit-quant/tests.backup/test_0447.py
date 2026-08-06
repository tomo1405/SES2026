import pytest
from src_0447 import task_func

def test_task_func():
    X, y, ax = task_func()
    assert len(X) == 100
    assert len(y) == 100
    assert len(ax.get_children()) == 1
    assert ax.get_children()[0].get_label() == 'scatter'