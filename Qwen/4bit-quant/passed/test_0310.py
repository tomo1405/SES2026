import pytest
from src_0310 import task_func

def test_task_func_with_non_empty_lists():
    input_data = [[1, 2, 3], [4, 5, 6]]
    expected_output = [[0.0, 0.3333333333333333, 0.6666666666666666], [0.0, 0.3333333333333333, 0.6666666666666666]]
    assert task_func(input_data) == expected_output

def test_task_func_with_empty_lists():
    input_data = [[], []]
    expected_output = [[0.2894736842105263, 0.5196078431372549, 0.7497400659340659, 0.9798722887308769, 1.0], 
                      [0.2894736842105263, 0.5196078431372549, 0.7497400659340659, 0.9798722887308769, 1.0]]
    assert task_func(input_data) == expected_output

def test_task_func_with_single_element_lists():
    input_data = [[1], [2]]
    expected_output = [[0.0], [1.0]]
    assert task_func(input_data) == expected_output

def test_task_func_with_large_numbers():
    input_data = [[1000, 2000, 3000], [4000, 5000, 6000]]
    expected_output = [[0.0, 0.3333333333333333, 0.6666666666666666], [0.0, 0.3333333333333333, 0.6666666666666666]]
    assert task_func(input_data) == expected_output

def test_task_func_with_seed_variation():
    input_data = [[1, 2, 3], [4, 5, 6]]
    expected_output = [[0.0, 0.3333333333333333, 0.6666666666666666], [0.0, 0.3333333333333333, 0.6666666666666666]]
    assert task_func(input_data, seed=42) == expected_output

def test_task_func_with_different_seed():
    input_data = [[1, 2, 3], [4, 5, 6]]
    expected_output = [[0.0, 0.3333333333333333, 0.6666666666666666], [0.0, 0.3333333333333333, 0.6666666666666666]]
    assert task_func(input_data, seed=100) != expected_output