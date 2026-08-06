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
    expected_result = 2
    assert task_func(L) == expected_result
    
    # Test case 4
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    expected_result = 5
    assert task_func(L) == expected_result
    
    # Test case 5
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    expected_result = 5
    assert task_func(L) == expected_result
    
    # Test case 6
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
    expected_result = 5
    assert task_func(L) == expected_result
    
    # Test case 7
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    expected_result = 5
    assert task_func(L) == expected_result