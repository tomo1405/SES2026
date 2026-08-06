import pytest
from src_0468 import task_func

def test_task_func():
    # Test case 1: n = 10, seed = 0
    n = 10
    seed = 0
    fig, points = task_func(n, seed)
    assert len(points) == n
    assert all(len(point) == 2 for point in points)
    assert all(0 <= point[0] <= 1 for point in points)
    assert all(0 <= point[1] <= 1 for point in points)

    # Test case 2: n = 10, seed = 1
    n = 10
    seed = 1
    fig, points = task_func(n, seed)
    assert len(points) == n
    assert all(len(point) == 2 for point in points)
    assert all(0 <= point[0] <= 1 for point in points)
    assert all(0 <= point[1] <= 1 for point in points)

    # Test case 3: n = 10, seed = 2
    n = 10
    seed = 2
    fig, points = task_func(n, seed)
    assert len(points) == n
    assert all(len(point) == 2 for point in points)
    assert all(0 <= point[0] <= 1 for point in points)
    assert all(0 <= point[1] <= 1 for point in points)

    # Test case 4: n = 10, seed = 3
    n = 10
    seed = 3
    fig, points = task_func(n, seed)
    assert len(points) == n
    assert all(len(point) == 2 for point in points)
    assert all(0 <= point[0] <= 1 for point in points)
    assert all(0 <= point[1] <= 1 for point in points)

    # Test case 5: n = 10, seed = 4
    n = 10
    seed = 4
    fig, points = task_func(n, seed)
    assert len(points) == n
    assert all(len(point) == 2 for point in points)
    assert all(0 <= point[0] <= 1 for point in points)
    assert all(0 <= point[1] <= 1 for point in points)

    # Test case 6: n = 10, seed = 5
    n = 10
    seed = 5
    fig, points = task_func(n, seed)
    assert len(points) == n
    assert all(len(point) == 2 for point in points)
    assert all(0 <= point[0] <= 1 for point in points)
    assert all(0 <= point[1] <= 1 for point in points)

    # Test case 7: n = 10, seed = 6
    n = 10
    seed = 6
    fig, points = task_func(n, seed)
    assert len(points) == n
    assert all(len(point) == 2 for point in points)
    assert all(0 <= point[0] <= 1 for point in points)
    assert all(0 <= point[1] <= 1 for point in points)

    # Test case 8: n = 10, seed = 7
    n = 10
    seed = 7
    fig, points = task_func(n, seed)
    assert len(points) == n
    assert all(len(point) == 2 for point in points)
    assert all(0 <= point[0] <= 1 for point in points)
    assert all(0 <= point[1] <= 1 for point in points)

    # Test case 9: n = 10, seed = 8
    n = 10
    seed = 8
    fig, points = task_func(n, seed)
    assert len(points) == n
    assert all(len(point) == 2 for point in points)
    assert all(0 <= point[0] <= 1 for point in points)
    assert all(0 <= point[1] <= 1 for point in points)

    # Test case 10: n = 10, seed = 9
    n = 10
    seed = 9
    fig, points = task_func(n, seed)
    assert len(points) == n
    assert all(len(point) == 2 for point in points)
    assert all(0 <= point[0] <= 1 for point in points)
    assert all(0 <= point[1] <= 1 for point in points)