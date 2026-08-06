python
import numpy as np
import math
import pytest

# Constants
POSSIBLE_NUMBERS = np.arange(1, 11)

def task_func(list_of_lists):
    sums = []
    for list_ in list_of_lists:
        sum_ = sum(math.pow(x, 2) for x in POSSIBLE_NUMBERS[:len(list_)])
        sums.append(sum_)

    return sums

def test_task_func():
    # Test case 1
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_result = [14, 55, 144]
    assert task_func(list_of_lists) == expected_result

    # Test case 2
    list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    expected_result = [14, 55, 144]
    assert task_func(list_of_lists) == expected_result

    # Test case 3
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
    expected_result = [14, 55, 144, 100]
    assert task_func(list_of_lists) == expected_result

    # Test case 4
    list_of_lists = []
    expected_result = []
    assert task_func(list_of_lists) == expected_result

    # Test case 5
    list_of_lists = [[]]
    expected_result = []
    assert task_func(list_of_lists) == expected_result

    # Test case 6
    list_of_lists = [[], []]
    expected_result = []
    assert task_func(list_of_lists) == expected_result

    # Test case 7
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10], []]
    expected_result = [14, 55, 144, 100]
    assert task_func(list_of_lists) == expected_result

    # Test case 8
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10], [11, 12, 13]]
    expected_result = [14, 55, 144, 100, 169]
    assert task_func(list_of_lists) == expected_result