import pytest
from src_0227 import task_func

def test_task_func():
    range_start = 0
    range_end = 10
    step = 0.1
    data, ax = task_func(range_start, range_end, step)
    assert isinstance(data, tuple)
    assert len(data) == 2
    assert isinstance(ax, object)
    assert ax.get_title() == "Exponential Function Plot"
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "e^x"