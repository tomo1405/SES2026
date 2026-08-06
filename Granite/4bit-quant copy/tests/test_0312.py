import numpy as np
import random
from scipy import stats
from src_0312 import task_func

def test_task_func():
    list_of_lists = [[1, 2, 3], [4, 5], [], [6, 7, 8, 9]]
    random.seed(0)
    expected_result = {
        'mean': 5.0,
        'median': 5.0,
        'mode': 1
    }
    result = task_func(list_of_lists)
    assert result == expected_result

def test_task_func_with_seed_1():
    list_of_lists = [[1, 2, 3], [4, 5], [], [6, 7, 8, 9]]
    random.seed(1)
    expected_result = {
        'mean': 5.0,
        'median': 5.0,
        'mode': 1
    }
    result = task_func(list_of_lists, seed=1)
    assert result == expected_result

def test_task_func_with_seed_2():
    list_of_lists = [[1, 2, 3], [4, 5], [], [6, 7, 8, 9]]
    random.seed(2)
    expected_result = {
        'mean': 5.0,
        'median': 5.0,
        'mode': 1
    }
    result = task_func(list_of_lists, seed=2)
    assert result == expected_result

def test_task_func_with_seed_3():
    list_of_lists = [[1, 2, 3], [4, 5], [], [6, 7, 8, 9]]
    random.seed(3)
    expected_result = {
        'mean': 5.0,
        'median': 5.0,
        'mode': 1
    }
    result = task_func(list_of_lists, seed=3)
    assert result == expected_result

def test_task_func_with_seed_4():
    list_of_lists = [[1, 2, 3], [4, 5], [], [6, 7, 8, 9]]
    random.seed(4)
    expected_result = {
        'mean': 5.0,
        'median': 5.0,
        'mode': 1
    }
    result = task_func(list_of_lists, seed=4)
    assert result == expected_result