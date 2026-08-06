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
        'Position 1': 5.5,
        'Position 2': 6.5,
        'Position 3': 7.5
    }
    results = task_func(data_list)
    assert results == expected_results
    assert os.path.exists("mean_values.json")
    with open("mean_values.json", 'r') as f:
        json_content = json.load(f)
    assert json_content == expected_results
    os.remove("mean_values.json")

def test_task_func_with_custom_json_file():
    data_list = [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ]
    custom_json_file_name = "custom_mean_values.json"
    expected_results = {
        'Position 1': 40.0,
        'Position 2': 50.0,
        'Position 3': 60.0
    }
    results = task_func(data_list, custom_json_file_name)
    assert results == expected_results
    assert os.path.exists(custom_json_file_name)
    with open(custom_json_file_name, 'r') as f:
        json_content = json.load(f)
    assert json_content == expected_results
    os.remove(custom_json_file_name)

def test_task_func_with_mismatched_lists():
    data_list = [
        [1, 2, 3],
        [4, 5],
        [6, 7, 8, 9]
    ]
    expected_results = {
        'Position 1': 3.6666666666666665,
        'Position 2': 4.0,
        'Position 3': 8.0,
        'Position 4': 9.0
    }
    results = task_func(data_list)
    assert results == expected_results
    assert os.path.exists("mean_values.json")
    with open("mean_values.json", 'r') as f:
        json_content = json.load(f)
    assert json_content == expected_results
    os.remove("mean_values.json")

def test_task_func_with_empty_lists():
    data_list = [
        [],
        [],
        []
    ]
    expected_results = {
        'Position 1': np.nan,
        'Position 2': np.nan,
        'Position 3': np.nan
    }
    results = task_func(data_list)
    assert np.allclose(list(results.values()), list(expected_results.values()), equal_nan=True)
    assert os.path.exists("mean_values.json")
    with open("mean_values.json", 'r') as f:
        json_content = json.load(f)
    assert all(np.isnan(v) for v in json_content.values())
    os.remove("mean_values.json")

def test_task_func_with_single_list():
    data_list = [
        [1, 2, 3]
    ]
    expected_results = {}
    results = task_func(data_list)
    assert results == expected_results
    assert os.path.exists("mean_values.json")
    with open("mean_values.json", 'r') as f:
        json_content = json.load(f)
    assert json_content == expected_results
    os.remove("mean_values.json")