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

# Test cases
def test_task_func_1():
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_result = [14, 55, 126]
    assert task_func(list_of_lists) == expected_result

def test_task_func_2():
    list_of_lists = [[1, 2], [3, 4, 5], [6, 7, 8, 9]]
    expected_result = [5, 29, 126]
    assert task_func(list_of_lists) == expected_result

def test_task_func_3():
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
    expected_result = [14, 55, 126, 100]
    assert task_func(list_of_lists) == expected_result

def test_task_func_4():
    list_of_lists = []
    expected_result = []
    assert task_func(list_of_lists) == expected_result

def test_task_func_5():
    list_of_lists = [[]]
    expected_result = [0]
    assert task_func(list_of_lists) == expected_result

def test_task_func_6():
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10], []]
    expected_result = [14, 55, 126, 100, 0]
    assert task_func(list_of_lists) == expected_result

# Run tests
if __name__ == '__main__':
    pytest.main(['-v', __file__])