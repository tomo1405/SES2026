python
import numpy as np
import itertools
import random
import statistics

def task_func(T1, RANGE=100):
    if len(T1) <= 0:
        raise statistics.StatisticsError
    int_list = [list(map(int, x)) for x in T1]
    flattened_list = list(itertools.chain(*int_list))
    total_nums = sum(flattened_list)
    random_nums = [random.randint(0, RANGE) for _ in range(total_nums)]
    mean = np.mean(random_nums)
    median = np.median(random_nums)
    mode = statistics.mode(random_nums)
    return mean, median, mode

def test_task_func():
    # Test case 1
    T1 = ['1 2 3', '4 5 6']
    mean, median, mode = task_func(T1)
    assert mean == 3.5
    assert median == 3
    assert mode == 3
    
    # Test case 2
    T1 = ['1 2 3', '4 5 6', '7 8 9']
    mean, median, mode = task_func(T1)
    assert mean == 5
    assert median == 5
    assert mode == 5
    
    # Test case 3
    T1 = []
    try:
        mean, median, mode = task_func(T1)
    except statistics.StatisticsError:
        assert True
    
    # Test case 4
    T1 = ['1 2 3', '4 5 6', 'a b c']
    try:
        mean, median, mode = task_func(T1)
    except ValueError:
        assert True