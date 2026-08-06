import pytest
from src_0310 import task_func

def test_task_func_with_non_empty_lists():
    input_data = [[1, 2, 3], [4, 5, 6]]
    expected_output = [[0.0, 0.3333333333333333, 0.6666666666666666], [0.0, 0.3333333333333333, 0.6666666666666666]]
    assert task_func(input_data) == expected_output

def test_task_func_with_empty_lists():
    input_data = [[], []]
    expected_output = [[0.0, 0.2, 0.4, 0.6, 0.8], [0.0, 0.2, 0.4, 0.6, 0.8]]
    assert task_func(input_data) == expected_output

def test_task_func_with_mixed_lists():
    input_data = [[1, 2, 3], [], [7, 8, 9]]
    expected_output = [[0.0, 0.3333333333333333, 0.6666666666666666], [0.0, 0.2, 0.4, 0.6, 0.8], [0.0, 0.3333333333333333, 0.6666666666666666]]
    assert task_func(input_data) == expected_output

def test_task_func_with_single_element_lists():
    input_data = [[5], [10], [15]]
    expected_output = [[0.0], [0.5], [1.0]]
    assert task_func(input_data) == expected_output

def test_task_func_with_identical_lists():
    input_data = [[1, 1, 1], [1, 1, 1]]
    expected_output = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
    assert task_func(input_data) == expected_output

def test_task_func_with_different_seed():
    input_data = [[1, 2, 3], [4, 5, 6]]
    seed = 123
    expected_output = [[0.0, 0.3333333333333333, 0.6666666666666666], [0.0, 0.3333333333333333, 0.6666666666666666]]
    assert task_func(input_data, seed=seed) == expected_output