import pytest
from src_0872 import task_func
import numpy as np

def test_task_func_with_valid_data():
    data_list = [(1, 2.5, 3), (4, 5, np.nan), (7, 8, 9)]
    file_name = 'test_output.txt'
    expected_mean_values = [5.5, 6.5]
    
    mean_values = task_func(data_list, file_name)
    
    assert mean_values == expected_mean_values
    
    with open(file_name, 'r') as f:
        content = f.read()
        assert content == 'Position 1: 5.5\nPosition 2: 6.5\n'

def test_task_func_with_no_numeric_data():
    data_list = [('a', 'b', 'c'), ('d', 'e', 'f')]
    file_name = 'test_output.txt'
    expected_mean_values = [np.nan, np.nan]
    
    mean_values = task_func(data_list, file_name)
    
    assert np.isnan(mean_values[0])
    assert np.isnan(mean_values[1])
    
    with open(file_name, 'r') as f:
        content = f.read()
        assert content == 'Position 1: nan\nPosition 2: nan\n'

def test_task_func_with_mixed_data_types():
    data_list = [(1, 'x', 3), (4, 5.5, np.nan), (7, 'y', 9)]
    file_name = 'test_output.txt'
    expected_mean_values = [5.5, 6.0]
    
    mean_values = task_func(data_list, file_name)
    
    assert mean_values == expected_mean_values
    
    with open(file_name, 'r') as f:
        content = f.read()
        assert content == 'Position 1: 5.5\nPosition 2: 6.0\n'

def test_task_func_with_empty_data_list():
    data_list = []
    file_name = 'test_output.txt'
    expected_mean_values = []
    
    mean_values = task_func(data_list, file_name)
    
    assert mean_values == expected_mean_values
    
    with open(file_name, 'r') as f:
        content = f.read()
        assert content == ''

def test_task_func_with_single_tuple():
    data_list = [(1, 2, 3)]
    file_name = 'test_output.txt'
    expected_mean_values = [2.0]
    
    mean_values = task_func(data_list, file_name)
    
    assert mean_values == expected_mean_values
    
    with open(file_name, 'r') as f:
        content = f.read()
        assert content == 'Position 1: 2.0\n'