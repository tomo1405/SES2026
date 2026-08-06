python
import numpy as np
import scipy.stats as stats
import pytest

def task_func(L):
    flattened = np.hstack(L)
    mode = stats.mode(flattened)[0][0]
    return mode

def test_task_func():
    # Test case 1
    L = [[1, 2, 3], [4, 5, 6]]
    assert task_func(L) == 3
    
    # Test case 2
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert task_func(L) == 3
    
    # Test case 3
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3]]
    assert task_func(L) == 3
    
    # Test case 4
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6]]
    assert task_func(L) == 3
    
    # Test case 5
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert task_func(L) == 3
    
    # Test case 6
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3]]
    assert task_func(L) == 3
    
    # Test case 7
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6]]
    assert task_func(L) == 3
    
    # Test case 8
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert task_func(L) == 3
    
    # Test case 9
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3]]
    assert task_func(L) == 3
    
    # Test case 10
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6]]
    assert task_func(L) == 3