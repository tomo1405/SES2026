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
    T1 = [['1', '2', '3'], ['4', '5', '6']]
    RANGE = 100
    mean, median, mode = task_func(T1, RANGE)
    assert mean == 45.0
    assert median == 45.0
    assert mode == [45]
    
    T1 = [['1', '2', '3'], ['4', '5', '6']]
    RANGE = 1000
    mean, median, mode = task_func(T1, RANGE)
    assert mean == 450.0
    assert median == 450.0
    assert mode == [450]
    
    T1 = []
    RANGE = 100
    try:
        mean, median, mode = task_func(T1, RANGE)
    except statistics.StatisticsError:
        assert True
        
    T1 = [['1', '2', '3'], ['4', '5', '6']]
    RANGE = -100
    try:
        mean, median, mode = task_func(T1, RANGE)
    except ValueError:
        assert True