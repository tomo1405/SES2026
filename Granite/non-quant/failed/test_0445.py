import pytest
from src_0445 import task_func

def test_task_func():
    points, ax = task_func()
    assert points.shape == (100, 3)
    assert ax.name == "3d"

def test_task_func_with_seed():
    points_1, ax_1 = task_func(random_seed=42)
    points_2, ax_2 = task_func(random_seed=42)
    assert np.array_equal(points_1, points_2)
    assert ax_1.name == ax_2.name