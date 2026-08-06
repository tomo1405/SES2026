import pytest
from src_0635 import task_func
import numpy as np
from scipy import stats

def test_task_func_single_element():
    input_list = [1]
    repetitions = 3
    expected_mode = stats.mode(np.array([1, 1, 1]))
    assert np.array_equal(task_func(input_list, repetitions).mode, expected_mode.mode)

def test_task_func_multiple_elements():
    input_list = [1, 2, 3]
    repetitions = 2
    expected_mode = stats.mode(np.array([1, 2, 3, 1, 2, 3]))
    assert np.array_equal(task_func(input_list, repetitions).mode, expected_mode.mode)

def test_task_func_repeated_elements():
    input_list = [2, 2, 3]
    repetitions = 4
    expected_mode = stats.mode(np.array([2, 2, 3, 2, 2, 3, 2, 2, 3, 2, 2, 3]))
    assert np.array_equal(task_func(input_list, repetitions).mode, expected_mode.mode)

def test_task_func_empty_list():
    input_list = []
    repetitions = 5
    expected_mode = stats.mode(np.array([]))
    assert np.array_equal(task_func(input_list, repetitions).mode, expected_mode.mode)

def test_task_func_single_repetition():
    input_list = [4, 5, 6]
    repetitions = 1
    expected_mode = stats.mode(np.array([4, 5, 6]))
    assert np.array_equal(task_func(input_list, repetitions).mode, expected_mode.mode)