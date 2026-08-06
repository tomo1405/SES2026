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
    assert all(point[0]**2 + point[1]**2 <= radius**2 for point in points)
    assert ax.get_xlim() == (-radius, radius)
    assert ax.get_ylim() == (-radius, radius)
    assert ax.get_aspect() == 'equal'
    assert ax.get_adjustable() == 'box'