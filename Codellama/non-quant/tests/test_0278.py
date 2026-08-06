import math
import random

from src_0278 import task_func


def test_task_func_n_less_than_2():
    n = 1
    points = [(random.random(), random.random()) for i in range(n)]
    closest_pair = task_func(n)
    assert closest_pair is None

def test_task_func_n_greater_than_2():
    n = 3
    points = [(random.random(), random.random()) for i in range(n)]
    closest_pair = task_func(n)
    assert closest_pair is not None
    assert len(closest_pair) == 2
    assert closest_pair[0][0] - closest_pair[1][0] == math.hypot(closest_pair[0][0] - closest_pair[1][0], closest_pair[0][1] - closest_pair[1][1])
    assert closest_pair[0][1] - closest_pair[1][1] == math.hypot(closest_pair[0][0] - closest_pair[1][0], closest_pair[0][1] - closest_pair[1][1])