import pytest
from src_0697 import task_func
import numpy as np
import math
import random
from random import uniform

def test_task_func_output_type():
    """
    Test if the output of task_func is a list of tuples
    """
    radius = 1.0
    num_points = 10
    output = task_func(radius, num_points)
    assert isinstance(output, list)
    assert all(isinstance(item, tuple) for item in output)

def test_task_func_num_points():
    """
    Test if the number of points returned by task_func is equal to the input
    """
    radius = 1.0
    num_points = 10
    output = task_func(radius, num_points)
    assert len(output) == num_points

def test_task_func_radius():
    """
    Test if the radius of points returned by task_func is within the input radius
    """
    radius = 1.0
    num_points = 10000
    output = task_func(radius, num_points)
    x_values = [item[0] for item in output]
    y_values = [item[1] for item in output]
    x_max = max(x_values)
    x_min = min(x_values)
    y_max = max(y_values)
    y_min = min(y_values)
    assert x_max <= radius and x_min >= -radius
    assert y_max <= radius and y_min >= -radius