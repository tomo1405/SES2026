import pytest
from src_0412 import task_func
import pandas as pd
import json
import os

def test_task_func_with_column_c():
    data = {
        "a": [1, 2, 3],
        "b": [4, 5, 6],
        "c": [7, 8, 9]
    }
    output_path = "test_output.json"
    result = task_func(data, output_path)
    
    assert result == output_path
    assert os.path.exists(output_path)
    
    with open(output_path, "r") as file:
        saved_data = json.load(file)
    
    expected_data = {
        "a": {0: 1, 1: 2, 2: 3},
        "b": {0: 4, 1: 5, 2: 6}
    }
    assert saved_data == expected_data
    
    os.remove(output_path)

def test_task_func_without_column_c():
    data = {
        "a": [1, 2, 3],
        "b": [4, 5, 6]
    }
    output_path = "test_output.json"
    result = task_func(data, output_path)
    
    assert result == output_path
    assert os.path.exists(output_path)
    
    with open(output_path, "r") as file:
        saved_data = json.load(file)
    
    expected_data = {
        "a": {0: 1, 1: 2, 2: 3},
        "b": {0: 4, 1: 5, 2: 6}
    }
    assert saved_data == expected_data
    
    os.remove(output_path)

def test_task_func_empty_data():
    data = {}
    output_path = "test_output.json"
    result = task_func(data, output_path)
    
    assert result == output_path
    assert os.path.exists(output_path)
    
    with open(output_path, "r") as file:
        saved_data = json.load(file)
    
    expected_data = {"a": {}, "b": {}}
    assert saved_data == expected_data
    
    os.remove(output_path)

def test_task_func_single_row():
    data = {
        "a": [1],
        "b": [4],
        "c": [7]
    }
    output_path = "test_output.json"
    result = task_func(data, output_path)
    
    assert result == output_path
    assert os.path.exists(output_path)
    
    with open(output_path, "r") as file:
        saved_data = json.load(file)
    
    expected_data = {
        "a": {0: 1},
        "b": {0: 4}
    }
    assert saved_data == expected_data
    
    os.remove(output_path)