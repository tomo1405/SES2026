import pytest
from src_1059 import task_func

def test_task_func():
    ax = task_func()
    assert ax is not None
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'
    assert ax.get_title() == 'Count'