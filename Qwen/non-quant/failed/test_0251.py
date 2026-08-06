import pytest
from src_0251 import task_func
import numpy as np
import json
import os

def test_task_func_with_default_json_file():
    data_list = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expected_results = {
        'Position 1': 5.0,
        'Position 2': 6.0,
        'Position 3': 7.0
    }
    
    results = task_func(data_list)
    assert results == expected_results
    
    with open('mean_values.json', 'r') as f:
        saved_results = json.load(f)
    assert saved_results == expected_results
    
    # Clean up the created file
    os.remove('mean_values.json')

def test_task_func_with_custom_json_file():
    data_list = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    custom_json_file = "custom_mean_values.json"
    expected_results = {
        'Position 1': 5.0,
        'Position 2': 6.0,
        'Position 3': 7.0
    }
    
    results = task_func(data_list, json_file_name=custom_json_file)
    assert results == expected_results
    
    with open(custom_json_file, 'r') as f:
        saved_results = json.load(f)
    assert saved_results == expected_results
    
    # Clean up the created file
    os.remove(custom_json_file)

def test_task_func_with_missing_data():
    data_list = [
        [1, 2, np.nan],
        [4, np.nan, 6],
        [np.nan, 8, 9]
    ]
    expected_results = {
        'Position 1': 2.0,
        'Position 2': 5.0,
        'Position 3': 7.5
    }
    
    results = task_func(data_list)
    assert results == expected_results
    
    with open('mean_values.json', 'r') as f:
        saved_results = json.load(f)
    assert saved_results == expected_results
    
    # Clean up the created file
    os.remove('mean_values.json')

def test_task_func_with_single_column():
    data_list = [
        [1, 2, 3]
    ]
    expected_results = {}
    
    results = task_func(data_list)
    assert results == expected_results
    
    with open('mean_values.json', 'r') as f:
        saved_results = json.load(f)
    assert saved_results == expected_results
    
    # Clean up the created file
    os.remove('mean_values.json')

def test_task_func_with_empty_data():
    data_list = []
    expected_results = {}
    
    results = task_func(data_list)
    assert results == expected_results
    
    with open('mean_values.json', 'r') as f:
        saved_results = json.load(f)
    assert saved_results == expected_results
    
    # Clean up the created file
    os.remove('mean_values.json')