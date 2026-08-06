python
import numpy as np
from itertools import combinations
import pytest

def task_func(array1, array2):
    if len(array1) != len(array2):
        raise ValueError("The input arrays must have the same length.")
    
    if len(array1) == 0:
        return 0
    
    max_distance = 0
    for comb in combinations(zip(array1, array2), 2):
        distance = np.linalg.norm(np.array(comb[0]) - np.array(comb[1]))
        if distance > max_distance:
            max_distance = distance

    return max_distance

def test_task_func():
    # Test case 1
    array1 = [1, 2, 3]
    array2 = [4, 5, 6]
    expected_result = 5.196152422706632
    assert task_func(array1, array2) == expected_result

    # Test case 2
    array1 = [1, 2, 3]
    array2 = [4, 5, 6, 7]
    with pytest.raises(ValueError):
        task_func(array1, array2)

    # Test case 3
    array1 = []
    array2 = []
    expected_result = 0
    assert task_func(array1, array2) == expected_result