import pytest
from src_0445 import task_func

def test_task_func():
    points, ax = task_func()
    assert points.shape == (100, 3)
    assert ax.name == "3d"