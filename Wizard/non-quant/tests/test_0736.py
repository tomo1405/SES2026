python
import numpy as np
from itertools import chain

def task_func(L):
    flattened = list(chain.from_iterable(L))
    mean = np.mean(flattened)
    variance = np.var(flattened)
    
    return {'mean': mean, 'variance': variance}

def test_task_func():
    # Test case 1
    L = [[1, 2, 3], [4, 5, 6]]
    expected_result = {'mean': 4.0, 'variance': 2.9166666666666665}
    assert task_func(L) == expected_result
    
    # Test case 2
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_result = {'mean': 5.0, 'variance': 3.3333333333333335}
    assert task_func(L) == expected_result
    
    # Test case 3
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    expected_result = {'mean': 6.0, 'variance': 3.75}
    assert task_func(L) == expected_result