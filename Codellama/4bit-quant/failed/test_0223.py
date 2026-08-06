import pytest
from src_0223 import task_func

def test_task_func():
    # Test case 1: input list is empty
    input_list = []
    expected_output = (None, None)
    assert task_func(input_list) == expected_output

    # Test case 2: input list has only one element
    input_list = [1]
    expected_output = (1, None)
    assert task_func(input_list) == expected_output

    # Test case 3: input list has multiple elements
    input_list = [1, 2, 3, 4, 5]
    expected_output = (1, 3, 6, 10, 15)
    assert task_func(input_list) == expected_output

    # Test case 4: input list has negative elements
    input_list = [-1, -2, -3, -4, -5]
    expected_output = (-1, -3, -6, -10, -15)
    assert task_func(input_list) == expected_output

    # Test case 5: input list has both positive and negative elements
    input_list = [1, -2, 3, -4, 5]
    expected_output = (1, -2, 1, -4, 6)
    assert task_func(input_list) == expected_output

    # Test case 6: input list has duplicate elements
    input_list = [1, 2, 3, 3, 4, 5]
    expected_output = (1, 3, 6, 9, 12, 15)
    assert task_func(input_list) == expected_output

    # Test case 7: input list has elements with different types
    input_list = [1, "2", 3, 4, 5]
    expected_output = (1, 3, 6, 10, 15)
    assert task_func(input_list) == expected_output

    # Test case 8: input list has elements with different types and duplicate elements
    input_list = [1, "2", 3, 3, 4, 5]
    expected_output = (1, 3, 6, 9, 12, 15)
    assert task_func(input_list) == expected_output

    # Test case 9: input list has elements with different types and negative elements
    input_list = [1, "2", -3, 4, 5]
    expected_output = (1, -3, 1, 4, 6)
    assert task_func(input_list) == expected_output

    # Test case 10: input list has elements with different types, negative elements, and duplicate elements
    input_list = [1, "2", -3, 3, 4, 5]
    expected_output = (1, -3, 1, 4, 9, 13)
    assert task_func(input_list) == expected_output