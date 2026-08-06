python
import pytest
from src_0862 import task_func

def test_task_func():
    # Test case 1
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_output = [{'apple': 1, 'banana': 1, 'cherry': 1}, {'apple': 1, 'banana': 1, 'cherry': 1}, {'apple': 1, 'banana': 1, 'cherry': 1}]
    assert task_func(list_of_lists) == expected_output

    # Test case 2
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    expected_output = [{'apple': 1, 'banana': 1, 'cherry': 1}, {'apple': 1, 'banana': 1, 'cherry': 1}, {'apple': 1, 'banana': 1, 'cherry': 1}, {'apple': 1, 'banana': 1, 'cherry': 1}]
    assert task_func(list_of_lists) == expected_output

    # Test case 3
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
    expected_output = [{'apple': 1, 'banana': 1, 'cherry': 1}, {'apple': 1, 'banana': 1, 'cherry': 1}, {'apple': 1, 'banana': 1, 'cherry': 1}, {'apple': 1, 'banana': 1, 'cherry': 1}, {'apple': 1, 'banana': 1, 'cherry': 1}]
    assert task_func(list_of_lists) == expected_output