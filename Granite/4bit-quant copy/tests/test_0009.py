import pytest
from collections import Counter
import itertools
from random import randint

def task_func(T1, RANGE=100):
    int_list = [list(map(int, x)) for x in T1]
    flattened_list = list(itertools.chain(*int_list))
    total_nums = sum(flattened_list)

    random_nums = [randint(0, RANGE) for _ in range(total_nums)]
    counts = Counter(random_nums)

    return counts

def test_task_func():
    T1 = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    expected_result = Counter({1: 10, 2: 10, 3: 10, 4: 10, 5: 10, 6: 10, 7: 10, 8: 10, 9: 10})
    actual_result = task_func(T1)
    assert actual_result == expected_result

def test_task_func_with_custom_range():
    T1 = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    RANGE = 50
    expected_result = Counter({1: 150, 2: 150, 3: 150, 4: 150, 5: 150})
    actual_result = task_func(T1, RANGE)
    assert actual_result == expected_result

def test_task_func_with_empty_input():
    T1 = []
    expected_result = Counter({})
    actual_result = task_func(T1)
    assert actual_result == expected_result