python
import numpy as np
import math
import random
from random import uniform
import pytest

def task_func(radius, num_points):
    out = []
    
    for _ in range(num_points):
        theta = uniform(0, 2*np.pi)
        r = radius * math.sqrt(uniform(0, 1))
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        out.append((x, y))
        
    return out

def test_task_func():
    assert task_func(1, 10) == [(0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0)]
    assert task_func(2, 5) == [(1.0, 0.0), (0.0, 2.0), (-1.0, 0.0), (0.0, -2.0), (2.0, 0.0)]
    assert task_func(3, 3) == [(2.0, 0.0), (0.0, 3.0), (-2.0, 0.0)]
    assert task_func(4, 2) == [(3.0, 0.0), (-3.0, 0.0)]
    assert task_func(5, 1) == [(4.0, 0.0)]