import pytest
from src_0278 import task_func

def test_task_func():
    # Test case 1: n < 2
    n = 1
    points = [(random.random(), random.random()) for i in range(n)]
    closest_pair = task_func(n)
    assert closest_pair is None

    # Test case 2: n >= 2
    n = 2
    points = [(random.random(), random.random()) for i in range(n)]
    closest_pair = task_func(n)
    assert closest_pair is not None
    assert len(closest_pair) == 2
    assert closest_pair[0][0] != closest_pair[1][0]
    assert closest_pair[0][1] != closest_pair[1][1]

    # Test case 3: n >= 3
    n = 3
    points = [(random.random(), random.random()) for i in range(n)]
    closest_pair = task_func(n)
    assert closest_pair is not None
    assert len(closest_pair) == 2
    assert closest_pair[0][0] != closest_pair[1][0]
    assert closest_pair[0][1] != closest_pair[1][1]

    # Test case 4: n >= 4
    n = 4
    points = [(random.random(), random.random()) for i in range(n)]
    closest_pair = task_func(n)
    assert closest_pair is not None
    assert len(closest_pair) == 2
    assert closest_pair[0][0] != closest_pair[1][0]
    assert closest_pair[0][1] != closest_pair[1][1]

    # Test case 5: n >= 5
    n = 5
    points = [(random.random(), random.random()) for i in range(n)]
    closest_pair = task_func(n)
    assert closest_pair is not None
    assert len(closest_pair) == 2
    assert closest_pair[0][0] != closest_pair[1][0]
    assert closest_pair[0][1] != closest_pair[1][1]