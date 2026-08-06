import numpy as np
import math
import random
from random import uniform
from src_0697 import task_func
import pytest

def test_task_func_output_type():
    radius = 1.0
    num_points = 10
    output = task_func(radius, num_points)
    assert isinstance(output, list), "Output should be a list"
    assert all(isinstance(point, tuple) for point in output), "Each point should be a tuple"
    assert all(len(point) == 2 for point in output), "Each point should have two elements"

def test_task_func_num_points():
    radius = 1.0
    num_points = 10
    output = task_func(radius, num_points)
    assert len(output) == num_points, "Number of points should match the input"

def test_task_func_radius():
    radius = 1.0
    num_points = 10
    output = task_func(radius, num_points)
    x_values = [point[0] for point in output]
    y_values = [point[1] for point in output]
    x_max = max(x_values)
    x_min = min(x_values)
    y_max = max(y_values)
    y_min = min(y_values)
    assert x_max <= radius and x_min >= -radius, "X-values should be within the radius"
    assert y_max <= radius and y_min >= -radius, "Y-values should be within the radius"

def test_task_func_uniformity():
    radius = 1.0
    num_points = 1000
    output = task_func(radius, num_points)
    x_values = [point[0] for point in output]
    y_values = [point[1] for point in output]
    x_mean = np.mean(x_values)
    y_mean = np.mean(y_values)
    assert abs(x_mean) < 0.1, "X-values should be uniformly distributed"
    assert abs(y_mean) < 0.1, "Y-values should be uniformly distributed"