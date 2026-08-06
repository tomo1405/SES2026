python
import numpy as np
import pytest
from scipy.stats import iqr

def task_func(L):
    flattened = np.array(L).flatten()
    iqr_value = iqr(flattened)
    
    return iqr_value

def test_task_func():
    # Test case 1
    L = [1, 2, 3, 4, 5]
    expected_result = 1
    assert task_func(L) == expected_result
    
    # Test case 2
    L = [10, 20, 30, 40, 50]
    expected_result = 10
    assert task_func(L) == expected_result
    
    # Test case 3
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected_result = 5
    assert task_func(L) == expected_result
    
    # Test case 4
    L = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    expected_result = 50
    assert task_func(L) == expected_result
    
    # Test case 5
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    expected_result = 8
    assert task_func(L) == expected_result
    
    # Test case 6
    L = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
    expected_result = 80
    assert task_func(L) == expected_result