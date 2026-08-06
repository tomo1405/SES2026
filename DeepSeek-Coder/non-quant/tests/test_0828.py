import pytest
from src_0828 import task_func

def test_task_func():
    # Test case 1: Normal case
    input_list = [3, 2, 5, 7, 11]
    expected_output = [2, 3, 5, 7, 11]
    assert task_func(input_list) == expected_output

    # Add more test cases as needed