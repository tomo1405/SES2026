import pytest
from src_0223 import task_func

def test_task_func():
    # Test case 1: empty list
    list_input = []
    expected_cumsum = []
    expected_ax = None
    assert task_func(list_input) == (expected_cumsum, expected_ax)

    # Test case 2: list with one element
    list_input = [1]
    expected_cumsum = [1]
    expected_ax = None
    assert task_func(list_input) == (expected_cumsum, expected_ax)

    # Test case 3: list with multiple elements
    list_input = [1, 2, 3, 4, 5]
    expected_cumsum = [1, 3, 6, 10, 15]
    expected_ax = None
    assert task_func(list_input) == (expected_cumsum, expected_ax)

    # Test case 4: list with negative elements
    list_input = [-1, -2, -3, -4, -5]
    expected_cumsum = [-1, -3, -6, -10, -15]
    expected_ax = None
    assert task_func(list_input) == (expected_cumsum, expected_ax)

    # Test case 5: list with mixed elements
    list_input = [1, 2, -3, 4, -5]
    expected_cumsum = [1, 3, -1, 7, -6]
    expected_ax = None
    assert task_func(list_input) == (expected_cumsum, expected_ax)