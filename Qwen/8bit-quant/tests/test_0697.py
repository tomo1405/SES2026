import math

from src_0697 import task_func


def test_task_func_output_length():
    radius = 5
    num_points = 10
    result = task_func(radius, num_points)
    assert len(result) == num_points

def test_task_func_output_type():
    radius = 5
    num_points = 10
    result = task_func(radius, num_points)
    assert all(isinstance(point, tuple) and len(point) == 2 for point in result)

def test_task_func_output_values():
    radius = 5
    num_points = 10
    result = task_func(radius, num_points)
    for x, y in result:
        assert math.sqrt(x**2 + y**2) <= radius

def test_task_func_zero_radius():
    radius = 0
    num_points = 10
    result = task_func(radius, num_points)
    assert all(x == 0 and y == 0 for x, y in result)

def test_task_func_negative_radius():
    radius = -5
    num_points = 10
    result = task_func(radius, num_points)
    assert all(x == 0 and y == 0 for x, y in result)

def test_task_func_zero_points():
    radius = 5
    num_points = 0
    result = task_func(radius, num_points)
    assert len(result) == 0

def test_task_func_one_point():
    radius = 5
    num_points = 1
    result = task_func(radius, num_points)
    assert len(result) == 1
    x, y = result[0]
    assert math.sqrt(x**2 + y**2) <= radius