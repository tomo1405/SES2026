import pytest
import random
import math
import matplotlib.pyplot as plt
from src_0319 import task_func

def test_task_func():
    points_count = 1000
    radius = 1
    points = [(radius * math.sqrt(random.random()) * math.cos(2 * math.pi * random.random()), 
               radius * math.sqrt(random.random()) * math.sin(2 * math.pi * random.random())) 
              for _ in range(points_count)]
    fig, ax = plt.subplots()
    ax.scatter(*zip(*points))
    ax.set_aspect('equal', adjustable='box')
    assert task_func(points_count, radius) == ax

def test_task_func_default_args():
    assert task_func() == task_func(1000, 1)

def test_task_func_invalid_args():
    with pytest.raises(ValueError):
        task_func(-1)
    with pytest.raises(ValueError):
        task_func(1000, -1)