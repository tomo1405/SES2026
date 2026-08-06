python
import numpy as np
import random
from scipy import stats

def task_func(list_of_lists, size=5, seed=0):
    random.seed(seed)
    data = []
    for list_ in list_of_lists:
        if list_:
            data += list_
        else:
            data += [random.randint(0, 100) for _ in range(size)]
    
    return {
        'mean': np.mean(data),
        'median': np.median(data),
        'mode': stats.mode(data)[0]
    }

def test_task_func():
    # Test case 1
    list_of_lists = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expected_result = {
        'mean': 5.0,
        'median': 5.0,
        'mode': 5
    }
    assert task_func(list_of_lists) == expected_result
    
    # Test case 2
    list_of_lists = [
        [],
        [],
        []
    ]
    expected_result = {
        'mean': 0.0,
        'median': 0.0,
        'mode': 0
    }
    assert task_func(list_of_lists) == expected_result
    
    # Test case 3
    list_of_lists = [
        [1, 2, 3],
        [],
        [4, 5, 6],
        [7, 8, 9],
        [],
        [10, 11, 12]
    ]
    expected_result = {
        'mean': 6.0,
        'median': 6.0,
        'mode': 6
    }
    assert task_func(list_of_lists) == expected_result
    
    # Test case 4
    list_of_lists = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18],
        [19, 20, 21],
        [22, 23, 24],
        [25, 26, 27],
        [28, 29, 30]
    ]
    expected_result = {
        'mean': 15.0,
        'median': 15.0,
        'mode': 15
    }
    assert task_func(list_of_lists) == expected_result