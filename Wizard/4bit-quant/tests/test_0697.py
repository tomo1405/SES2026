python
import numpy as np
import math
import random
from random import uniform

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
    # Test case 1
    assert task_func(1, 1) == [(0.0, 0.0)]
    
    # Test case 2
    assert task_func(2, 2) == [(1.0, 0.0), (0.0, 1.0)]
    
    # Test case 3
    assert task_func(3, 3) == [(2.0, 0.0), (1.0, 1.7320508075688772), (0.0, 3.0)]
    
    # Test case 4
    assert task_func(4, 4) == [(3.0, 0.0), (2.0, 1.7320508075688772), (1.0, 3.0), (0.0, 4.0)]
    
    # Test case 5
    assert task_func(5, 5) == [(4.0, 0.0), (3.0, 1.7320508075688772), (2.0, 3.0), (1.0, 4.0), (0.0, 5.0)]
    
    # Test case 6
    assert task_func(6, 6) == [(5.0, 0.0), (4.0, 1.7320508075688772), (3.0, 3.0), (2.0, 4.0), (1.0, 5.0), (0.0, 6.0)]
    
    # Test case 7
    assert task_func(7, 7) == [(6.0, 0.0), (5.0, 1.7320508075688772), (4.0, 3.0), (3.0, 4.0), (2.0, 5.0), (1.0, 6.0), (0.0, 7.0)]
    
    # Test case 8
    assert task_func(8, 8) == [(7.0, 0.0), (6.0, 1.7320508075688772), (5.0, 3.0), (4.0, 4.0), (3.0, 5.0), (2.0, 6.0), (1.0, 7.0), (0.0, 8.0)]
    
    # Test case 9
    assert task_func(9, 9) == [(8.0, 0.0), (7.0, 1.7320508075688772), (6.0, 3.0), (5.0, 4.0), (4.0, 5.0), (3.0, 6.0), (2.0, 7.0), (1.0, 8.0), (0.0, 9.0)]
    
    # Test case 10
    assert task_func(10, 10) == [(9.0, 0.0), (8.0, 1.7320508075688772), (7.0, 3.0), (6.0, 4.0), (5.0, 5.0), (4.0, 6.0), (3.0, 7.0), (2.0, 8.0), (1.0, 9.0), (0.0, 10.0)]