import pytest
from src_0278 import task_func

def test_task_func_with_n_less_than_2():
    assert task_func(1) is None
    assert task_func(0) is None

def test_task_func_with_n_greater_than_2():
    points = [(random.random(), random.random()) for i in range(3)]
    closest_pair = min(combinations(points, 2), key=lambda pair: math.hypot(pair[0][0] - pair[1][0], pair[0][1] - pair[1][1]))
    assert task_func(3) == closest_pair

def test_task_func_with_n_equal_to_2():
    points = [(random.random(), random.random()) for i in range(2)]
    closest_pair = min(combinations(points, 2), key=lambda pair: math.hypot(pair[0][0] - pair[1][0], pair[0][1] - pair[1][1]))
    assert task_func(2) == closest_pair