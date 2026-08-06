import pytest
from src_0220 import task_func
import math
import statistics
import numpy as np

def test_task_func():
    input_list = [1, 2, 3, 4, 5]
    expected_output = (2.5, 3, 3, 2, 3, 3)
    assert task_func(input_list) == expected_output

    input_list = [1, 2, 3, 4, 5, 6]
    expected_output = (3.5, 4, 4, 3, 4, 4)
    assert task_func(input_list) == expected_output

    input_list = [1, 2, 3, 4, 5, 6, 7]
    expected_output = (4.5, 5, 5, 4, 5, 5)
    assert task_func(input_list) == expected_output

    input_list = [1, 2, 3, 4, 5, 6, 7, 8]
    expected_output = (5.5, 6, 6, 5, 6, 6)
    assert task_func(input_list) == expected_output

    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected_output = (6.5, 7, 7, 6, 7, 7)
    assert task_func(input_list) == expected_output

    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected_output = (7.5, 8, 8, 7, 8, 8)
    assert task_func(input_list) == expected_output