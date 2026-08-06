import numpy as np
from scipy import stats
from src_0635 import task_func


def test_task_func_with_single_element():
    input_list = [42]
    repetitions = 3
    expected_mode = stats.mode(np.array([42, 42, 42]))
    assert task_func(input_list, repetitions).mode == expected_mode.mode
    assert task_func(input_list, repetitions).count == expected_mode.count

def test_task_func_with_multiple_elements():
    input_list = [1, 2, 3]
    repetitions = 2
    expected_mode = stats.mode(np.array([1, 2, 3, 1, 2, 3]))
    assert task_func(input_list, repetitions).mode == expected_mode.mode
    assert task_func(input_list, repetitions).count == expected_mode.count

def test_task_func_with_repeated_elements():
    input_list = [5, 5, 5]
    repetitions = 1
    expected_mode = stats.mode(np.array([5, 5, 5]))
    assert task_func(input_list, repetitions).mode == expected_mode.mode
    assert task_func(input_list, repetitions).count == expected_mode.count

def test_task_func_with_empty_list():
    input_list = []
    repetitions = 5
    expected_mode = stats.mode(np.array([]))
    assert task_func(input_list, repetitions).mode == expected_mode.mode
    assert task_func(input_list, repetitions).count == expected_mode.count

def test_task_func_with_single_repetition():
    input_list = [7, 8, 9]
    repetitions = 1
    expected_mode = stats.mode(np.array([7, 8, 9]))
    assert task_func(input_list, repetitions).mode == expected_mode.mode
    assert task_func(input_list, repetitions).count == expected_mode.count

def test_task_func_with_no_repetitions():
    input_list = [10, 11, 12]
    repetitions = 0
    expected_mode = stats.mode(np.array([]))
    assert task_func(input_list, repetitions).mode == expected_mode.mode
    assert task_func(input_list, repetitions).count == expected_mode.count