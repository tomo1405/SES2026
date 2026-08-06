import random
import math
import matplotlib.pyplot as plt
from src_0319 import task_func
import pytest

def test_task_func():
    points_count = 1000
    radius = 1
    points = [(radius * math.sqrt(random.random()) * math.cos(2 * math.pi * random.random()), 
               radius * math.sqrt(random.random()) * math.sin(2 * math.pi * random.random())) 
              for _ in range(points_count)]
    ax = task_func(points_count, radius)
    assert ax.get_aspect() == 'equal'
    assert ax.collections[0].get_offsets().shape == (points_count, 2)

def test_task_func_with_default_args():
    ax = task_func()
    assert ax.get_aspect() == 'equal'

def test_task_func_with_zero_points():
    ax = task_func(0)
    assert ax.collections[0].get_offsets().shape == (0, 2)

def test_task_func_with_negative_points():
    with pytest.raises(ValueError):
        task_func(-1)