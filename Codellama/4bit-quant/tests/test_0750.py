import pytest
from src_0750 import task_func

def test_task_func():
    myList = [1, 2, 3, 4, 5]
    expected_output = [0.2, 0.4, 0.6, 0.8, 1.0]
    assert task_func(myList) == expected_output

def test_task_func_with_different_input():
    myList = [1, 2, 3, 4, 5, 6]
    expected_output = [0.1, 0.3, 0.5, 0.7, 0.9, 1.0]
    assert task_func(myList) == expected_output

def test_task_func_with_empty_input():
    myList = []
    expected_output = []
    assert task_func(myList) == expected_output

def test_task_func_with_single_element_input():
    myList = [1]
    expected_output = [0.2]
    assert task_func(myList) == expected_output