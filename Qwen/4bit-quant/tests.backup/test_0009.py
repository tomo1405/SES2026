import pytest
from src_0009 import task_func
from collections import Counter
from random import randint

def test_task_func_with_empty_input():
    T1 = []
    result = task_func(T1)
    assert isinstance(result, Counter)
    assert len(result) == 0

def test_task_func_with_single_element():
    T1 = [['1', '2', '3']]
    result = task_func(T1)
    assert isinstance(result, Counter)
    assert all(isinstance(k, int) and k >= 0 and k <= 100 for k in result.keys())

def test_task_func_with_multiple_elements():
    T1 = [['1', '2'], ['3', '4', '5']]
    result = task_func(T1)
    assert isinstance(result, Counter)
    assert all(isinstance(k, int) and k >= 0 and k <= 100 for k in result.keys())

def test_task_func_with_zero_sum():
    T1 = [['0', '0'], ['0', '0']]
    result = task_func(T1)
    assert isinstance(result, Counter)
    assert len(result) == 0

def test_task_func_with_large_numbers():
    T1 = [['100', '200'], ['300', '400', '500']]
    result = task_func(T1)
    assert isinstance(result, Counter)
    assert all(isinstance(k, int) and k >= 0 and k <= 100 for k in result.keys())

def test_task_func_with_custom_range():
    T1 = [['1', '2', '3']]
    custom_range = 50
    result = task_func(T1, RANGE=custom_range)
    assert isinstance(result, Counter)
    assert all(isinstance(k, int) and k >= 0 and k <= custom_range for k in result.keys())