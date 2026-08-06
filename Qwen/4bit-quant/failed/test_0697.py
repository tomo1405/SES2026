import pytest
from src_0697 import task_func
import numpy as np
import math

def test_task_func_zero_radius():
    result = task_func(0, 5)
    assert len(result) == 5, "The number of points should match the input"
    assert all([math.isclose(x, 0) and math.isclose(y, 0) for x, y in result]), "All points should be at the origin"

def test_task_func_negative_radius():
    with pytest.raises(ValueError):
        task_func(-1, 5)

def test_task_func_zero_points():
    result = task_func(5, 0)
    assert len(result) == 0, "No points should be generated"

def test_task_func_positive_radius():
    result = task_func(5, 5)
    assert len(result) == 5, "The number of points should match the input"
    for x, y in result:
        assert math.isclose(x**2 + y**2, 25, rel_tol=1e-9), "Points should lie within the circle of radius 5"

def test_task_func_large_number_of_points():
    result = task_func(1, 1000)
    assert len(result) == 1000, "The number of points should match the input"
    for x, y in result:
        assert x**2 + y**2 <= 1, "Points should lie within the unit circle"