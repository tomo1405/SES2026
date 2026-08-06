import pytest
from src_0227 import task_func

def test_task_func():
    data, ax = task_func()
    assert data is not None
    assert ax is not None
    assert len(data) == 10
    assert ax.get_title() == "Exponential Function Plot"
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "e^x"