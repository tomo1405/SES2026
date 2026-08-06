import pytest
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

    assert len(points) == points_count
    assert all(math.sqrt(x**2 + y**2) <= radius for x, y in points)
    assert ax.get_aspect() == 'equal'
    assert ax.get_adjustable() == 'box'