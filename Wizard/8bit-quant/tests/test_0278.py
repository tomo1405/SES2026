python
import random
import itertools
import math

from src_0278 import task_func

def test_task_func():
    n = 10
    points = [(random.random(), random.random()) for i in range(n)]
    closest_pair = min(itertools.combinations(points, 2), key=lambda pair: math.hypot(pair[0][0] - pair[1][0], pair[0][1] - pair[1][1]))
    assert task_func(n) == closest_pair