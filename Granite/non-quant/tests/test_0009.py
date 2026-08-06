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
    expected_output = Counter({randint(0, 100): 3, randint(0, 100): 3, randint(0, 100): 3})
    actual_output = task_func(T1)
    assert actual_output == expected_output

def test_task_func_with_empty_input():
    T1 = []
    expected_output = Counter({})
    actual_output = task_func(T1)
    assert actual_output == expected_output

def test_task_func_with_negative_numbers():
    T1 = [['-1', '2', '3'], ['4', '-5', '6'], ['7', '8', '-9']]
    expected_output = Counter({randint(0, 100): 6, randint(0, 100): 6, randint(0, 100): 6})
    actual_output = task_func(T1)
    assert actual_output == expected_output