import pytest
from src_0011 import task_func
import numpy as np
import itertools
import random
import statistics

def test_task_func_with_valid_input():
    T1 = [['1', '2', '3'], ['4', '5']]
    mean, median, mode = task_func(T1)
    assert isinstance(mean, float)
    assert isinstance(median, float)
    assert isinstance(mode, int)

def test_task_func_with_empty_input():
    with pytest.raises(statistics.StatisticsError):
        task_func([])

def test_task_func_with_single_element():
    T1 = [['10']]
    mean, median, mode = task_func(T1)
    assert isinstance(mean, float)
    assert isinstance(median, float)
    assert isinstance(mode, int)

def test_task_func_with_large_numbers():
    T1 = [['100', '200', '300'], ['400', '500']]
    mean, median, mode = task_func(T1)
    assert isinstance(mean, float)
    assert isinstance(median, float)
    assert isinstance(mode, int)

def test_task_func_with_zero_sum():
    T1 = [['0', '0', '0'], ['0', '0']]
    mean, median, mode = task_func(T1)
    assert mean == 0
    assert median == 0
    assert mode == 0

def test_task_func_with_negative_numbers():
    T1 = [['-1', '-2', '-3'], ['-4', '-5']]
    mean, median, mode = task_func(T1)
    assert isinstance(mean, float)
    assert isinstance(median, float)
    assert isinstance(mode, int)

def test_task_func_with_non_integer_strings():
    T1 = [['1.5', '2.5'], ['3.5', '4.5']]
    with pytest.raises(ValueError):
        task_func(T1)

def test_task_func_with_large_range():
    T1 = [['1', '2'], ['3', '4']]
    mean, median, mode = task_func(T1, RANGE=1000)
    assert isinstance(mean, float)
    assert isinstance(median, float)
    assert isinstance(mode, int)