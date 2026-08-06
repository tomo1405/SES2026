import pytest
from src_0319 import task_func

def test_task_func():
    ax = task_func()
    assert ax is not None
    assert ax.get_title() == 'Scatter plot'
    assert ax.get_xlabel() == 'X axis'
    assert ax.get_ylabel() == 'Y axis'