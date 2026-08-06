python
import random
import math
import matplotlib.pyplot as plt
import pytest

def task_func(points_count=1000, radius=1):

    points = [(radius * math.sqrt(random.random()) * math.cos(2 * math.pi * random.random()), 
               radius * math.sqrt(random.random()) * math.sin(2 * math.pi * random.random())) 
              for _ in range(points_count)]

    fig, ax = plt.subplots()
    ax.scatter(*zip(*points))
    ax.set_aspect('equal', adjustable='box')
    return ax

def test_task_func():
    ax = task_func()
    assert isinstance(ax, plt.Axes)
    assert len(ax.collections) == 1
    assert isinstance(ax.collections[0], plt.collections.PathCollection)
    assert len(ax.collections[0].get_offsets()) == 1000