import pytest
from src_0220 import task_func
import math
import statistics
import numpy as np

def test_task_func():
    input_list = [math.pi, math.e, math.sqrt(2), 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected_output = (
        4.577215664901533,
        4.5,
        1,
        5,
        5,
        5
    )
    output = task_func(input_list)
    assert output == expected_output

def test_task_func_with_negative_numbers():
    input_list = [-math.pi, -math.e, -math.sqrt(2), -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
    expected_output = (
        -4.577215664901533,
        -4.5,
        -1,
        5,
        5,
        5
    )
    output = task_func(input_list)
    assert output == expected_output

def test_task_func_with_zero():
    input_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    expected_output = (
        0,
        0,
        0,
        0,
        0,
        0
    )
    output = task_func(input_list)
    assert output == expected_output

def test_task_func_with_one_element():
    input_list = [math.pi]
    expected_output = (
        math.pi,
        math.pi,
        math.pi,
        1,
        1,
        1
    )
    output = task_func(input_list)
    assert output == expected_output

def test_task_func_with_empty_list():
    input_list = []
    expected_output = (
        None,
        None,
        None,
        None,
        None,
        None
    )
    output = task_func(input_list)
    assert output == expected_output