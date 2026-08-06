import pytest
from src_0828 import task_func
import math
from sympy import isprime

def test_task_func():
    input_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    expected_output = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert task_func(input_list) == expected_output

def test_task_func_with_duplicates():
    input_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    expected_output = [2, 2, 3, 3, 5, 5, 7, 7, 11, 11, 13, 13, 17, 17, 19, 19, 23, 23, 29, 29]
    assert task_func(input_list) == expected_output

def test_task_func_with_negative_numbers():
    input_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, -2, -3, -5, -7, -11, -13, -17, -19, -23, -29]
    expected_output = [-29, -23, -19, -17, -13, -11, -7, -5, -3, -2, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert task_func(input_list) == expected_output

def test_task_func_with_non_prime_numbers():
    input_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]
    expected_output = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 4]
    assert task_func(input_list) == expected_output