import pytest
from src_0376 import task_func

def test_task_func():
    # Test case 1: Test with a 2D list of numbers
    input_list = [[1, 2], [3, 4], [5, 6]]
    expected_output = 'ax'  # Replace with the expected output of the function
    actual_output = task_func(input_list)
    assert actual_output == expected_output

    # Test case 2: Test with an empty list
    input_list = []
    expected_output = 'ax'  # Replace with the expected output of the function
    actual_output = task_func(input_list)
    assert actual_output == expected_output

    # Test case 3: Test with a list of lists of different lengths
    input_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    expected_output = 'ax'  # Replace with the expected output of the function
    actual_output = task_func(input_list)
    assert actual_output == expected_output