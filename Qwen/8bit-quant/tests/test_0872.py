import pytest
from src_0872 import task_func
import numpy as np

def test_task_func_with_valid_data():
    data_list = [
        ('Header', 1, 2, 3),
        ('Row1', 4, 5, 6),
        ('Row2', 7, 8, 9)
    ]
    file_name = 'test_output.txt'
    expected_mean_values = [np.mean([4, 7]), np.mean([5, 8]), np.mean([6, 9])]
    
    mean_values = task_func(data_list, file_name)
    
    assert np.allclose(mean_values, expected_mean_values)
    
    with open(file_name, 'r') as f:
        content = f.read()
        expected_content = (
            'Position 1: 5.5\n'
            'Position 2: 6.5\n'
            'Position 3: 7.5\n'
        )
        assert content == expected_content

def test_task_func_with_missing_values():
    data_list = [
        ('Header', 1, 2, 3),
        ('Row1', 4, None, 6),
        ('Row2', None, 8, 9)
    ]
    file_name = 'test_output_missing.txt'
    expected_mean_values = [np.nanmean([4, np.nan]), np.nanmean([np.nan, 8]), np.nanmean([6, 9])]
    
    mean_values = task_func(data_list, file_name)
    
    assert np.allclose(mean_values, expected_mean_values, equal_nan=True)
    
    with open(file_name, 'r') as f:
        content = f.read()
        expected_content = (
            'Position 1: nan\n'
            'Position 2: 8.0\n'
            'Position 3: 7.5\n'
        )
        assert content == expected_content

def test_task_func_with_empty_data():
    data_list = [
        ('Header', 1, 2, 3),
        ('Row1', None, None, None),
        ('Row2', None, None, None)
    ]
    file_name = 'test_output_empty.txt'
    expected_mean_values = [np.nan, np.nan, np.nan]
    
    mean_values = task_func(data_list, file_name)
    
    assert np.allclose(mean_values, expected_mean_values, equal_nan=True)
    
    with open(file_name, 'r') as f:
        content = f.read()
        expected_content = (
            'Position 1: nan\n'
            'Position 2: nan\n'
            'Position 3: nan\n'
        )
        assert content == expected_content

def test_task_func_with_single_row():
    data_list = [
        ('Header', 1, 2, 3),
        ('Row1', 4, 5, 6)
    ]
    file_name = 'test_output_single_row.txt'
    expected_mean_values = [np.nanmean([4]), np.nanmean([5]), np.nanmean([6])]
    
    mean_values = task_func(data_list, file_name)
    
    assert np.allclose(mean_values, expected_mean_values, equal_nan=True)
    
    with open(file_name, 'r') as f:
        content = f.read()
        expected_content = (
            'Position 1: 4.0\n'
            'Position 2: 5.0\n'
            'Position 3: 6.0\n'
        )
        assert content == expected_content