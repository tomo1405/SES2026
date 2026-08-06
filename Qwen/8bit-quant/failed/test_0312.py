import pytest
from src_0312 import task_func
import numpy as np
from scipy import stats

def test_task_func_with_non_empty_lists():
    input_data = [[1, 2, 3], [4, 5, 6]]
    expected_output = {
        'mean': np.mean([1, 2, 3, 4, 5, 6]),
        'median': np.median([1, 2, 3, 4, 5, 6]),
        'mode': stats.mode([1, 2, 3, 4, 5, 6])[0][0]
    }
    assert task_func(input_data) == expected_output

def test_task_func_with_empty_list_and_default_size():
    input_data = [[], [7, 8, 9]]
    expected_output = {
        'mean': np.mean([7, 8, 9] + [0, 0, 0, 0, 0]),  # Assuming default seed=0, random integers will be 0
        'median': np.median([7, 8, 9] + [0, 0, 0, 0, 0]),
        'mode': stats.mode([7, 8, 9] + [0, 0, 0, 0, 0])[0][0]
    }
    assert task_func(input_data) == expected_output

def test_task_func_with_empty_list_and_custom_size():
    input_data = [[], []]
    size = 3
    expected_output = {
        'mean': np.mean([0, 0, 0, 0, 0, 0]),  # Assuming default seed=0, random integers will be 0
        'median': np.median([0, 0, 0, 0, 0, 0]),
        'mode': stats.mode([0, 0, 0, 0, 0, 0])[0][0]
    }
    assert task_func(input_data, size=size) == expected_output

def test_task_func_with_custom_seed():
    input_data = [[], [10, 20, 30]]
    seed = 42
    expected_output = {
        'mean': np.mean([10, 20, 30] + [4, 2, 8]),  # Random integers with seed=42
        'median': np.median([10, 20, 30] + [4, 2, 8]),
        'mode': stats.mode([10, 20, 30] + [4, 2, 8])[0][0]
    }
    assert task_func(input_data, seed=seed) == expected_output

def test_task_func_with_all_empty_lists():
    input_data = [[], [], []]
    expected_output = {
        'mean': np.mean([0, 0, 0, 0, 0]),  # Assuming default seed=0, random integers will be 0
        'median': np.median([0, 0, 0, 0, 0]),
        'mode': stats.mode([0, 0, 0, 0, 0])[0][0]
    }
    assert task_func(input_data) == expected_output