import numpy as np
import math
from src_0864 import task_func

POSSIBLE_NUMBERS = np.arange(1, 11)

def test_task_func():
    list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9, 10]]
    expected_sums = [55, 55, 110]
    actual_sums = task_func(list_of_lists)
    assert actual_sums == expected_sums

def test_task_func_with_empty_list():
    list_of_lists = [[], [1, 2], []]
    expected_sums = [0, 5, 0]
    actual_sums = task_func(list_of_lists)
    assert actual_sums == expected_sums

def test_task_func_with_single_element_list():
    list_of_lists = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
    expected_sums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    actual_sums = task_func(list_of_lists)
    assert actual_sums == expected_sums