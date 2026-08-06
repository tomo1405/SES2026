import pytest
from src_0125 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    my_list = [1, 2, 3, 4, 5]
    result = task_func(my_list=my_list)
    assert isinstance(result, tuple), "The function should return a tuple."
    assert len(result) == 2, "The function should return a tuple with two elements."

    # Add more test cases as needed

    # Add more test cases to cover different scenarios