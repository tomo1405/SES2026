import pytest
from src_0251 import task_func
import numpy as np
import json

def test_task_func_with_default_json_file():
    data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_mean_values = {
        'Position 1': 5.0,
        'Position 2': 6.0,
        'Position 3': 7.0
    }
    
    result = task_func(data_list)
    
    assert result == expected_mean_values
    
    with open('mean_values.json', 'r') as f:
        json_content = json.load(f)
    
    assert json_content == expected_mean_values

def test_task_func_with_custom_json_file():
    data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    custom_json_file_name = "custom_mean_values.json"
    expected_mean_values = {
        'Position 1': 5.0,
        'Position 2': 6.0,
        'Position 3': 7.0
    }
    
    result = task_func(data_list, json_file_name=custom_json_file_name)
    
    assert result == expected_mean_values
    
    with open(custom_json_file_name, 'r') as f:
        json_content = json.load(f)
    
    assert json_content == expected_mean_values

def test_task_func_with_missing_values():
    data_list = [[1, 2, np.nan], [4, np.nan, 6], [np.nan, 8, 9]]
    expected_mean_values = {
        'Position 1': 2.0,
        'Position 2': 5.0,
        'Position 3': 7.5
    }
    
    result = task_func(data_list)
    
    assert result == expected_mean_values
    
    with open('mean_values.json', 'r') as f:
        json_content = json.load(f)
    
    assert json_content == expected_mean_values

def test_task_func_with_single_column():
    data_list = [[1, 2, 3]]
    expected_mean_values = {
        'Position 1': 2.0
    }
    
    result = task_func(data_list)
    
    assert result == expected_mean_values
    
    with open('mean_values.json', 'r') as f:
        json_content = json.load(f)
    
    assert json_content == expected_mean_values

def test_task_func_with_empty_data_list():
    data_list = []
    expected_mean_values = {}
    
    result = task_func(data_list)
    
    assert result == expected_mean_values
    
    with open('mean_values.json', 'r') as f:
        json_content = json.load(f)
    
    assert json_content == expected_mean_values