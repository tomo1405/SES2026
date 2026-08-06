import numpy as np
import random
from scipy import stats
from src_0312 import task_func

def test_task_func():
    list_of_lists = [[1, 2, 3], [4, 5, 6], [], [7, 8, 9]]
    random.seed(0)
    expected_result = {
        'mean': 5,
        'median': 5,
        'mode': 1
    }
    result = task_func(list_of_lists)
    assert result == expected_result

def test_task_func_with_seed_1():
    list_of_lists = [[1, 2, 3], [4, 5, 6], [], [7, 8, 9]]
    random.seed(1)
    expected_result = {
        'mean': 5.0,
        'median': 5.0,
        'mode': 1
    }
    result = task_func(list_of_lists, seed=1)
    assert result == expected_result

def test_task_func_with_seed_0_and_size_10():
    list_of_lists = [[1, 2, 3], [4, 5, 6], [], [7, 8, 9]]
    random.seed(0)
    expected_result = {
        'mean': 5.0,
        'median': 5.0,
        'mode': 1
    }
    result = task_func(list_of_lists, size=10, seed=0)
    assert result == expected_result

def test_task_func_with_empty_list_of_lists():
    list_of_lists = []
    random.seed(0)
    expected_result = {
        'mean': 50.5,
        'median': 50,
        'mode': 50
    }
    result = task_func(list_of_lists)
    assert result == expected_result