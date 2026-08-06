import pytest
from src_0220 import task_func
import math
import numpy as np

def test_task_func():
    input_list = [1, 2, 3, 4, 5]
    expected_output = (2.5, 3, 3, 2.5, 3, 3)
    assert task_func(input_list) == expected_output

def test_task_func_empty_input():
    input_list = []
    expected_output = (None, None, None, None, None, None)
    assert task_func(input_list) == expected_output

def test_task_func_invalid_input():
    input_list = [1, 2, 3, 4, "a"]
    expected_output = (None, None, None, None, None, None)
    assert task_func(input_list) == expected_output

def test_task_func_invalid_input_type():
    input_list = [1, 2, 3, 4, 5.5]
    expected_output = (None, None, None, None, None, None)
    assert task_func(input_list) == expected_output

def test_task_func_invalid_input_range():
    input_list = [1, 2, 3, 4, 100]
    expected_output = (None, None, None, None, None, None)
    assert task_func(input_list) == expected_output