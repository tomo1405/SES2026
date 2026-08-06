import pytest
from src_0406 import task_func

def test_task_func():
    points = 10
    y, ax = task_func(points)
    assert len(y) == points
    assert ax.get_xlabel() == 'x-axis'
    assert ax.get_ylabel() == 'y-axis'