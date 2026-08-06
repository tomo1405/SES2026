import pandas as pd
import json
from src_0412 import task_func

def test_task_func():
    data = {"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]}
    output_path = "./default_data_output.json"
    expected_output_path = "./default_data_output.json"
    actual_output_path = task_func(data, output_path)
    assert actual_output_path == expected_output_path
    with open(actual_output_path, "r") as file:
        data_dict = json.load(file)
    expected_data_dict = {"a": [1, 2, 3], "b": [4, 5, 6]}
    assert data_dict == expected_data_dict

def test_task_func_with_output_path():
    data = {"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]}
    output_path = "./custom_data_output.json"
    expected_output_path = "./custom_data_output.json"
    actual_output_path = task_func(data, output_path)
    assert actual_output_path == expected_output_path
    with open(actual_output_path, "r") as file:
        data_dict = json.load(file)
    expected_data_dict = {"a": [1, 2, 3], "b": [4, 5, 6]}
    assert data_dict == expected_data_dict

def test_task_func_with_invalid_data():
    data = {"a": [1, 2, 3], "b": [4, 5, 6]}
    output_path = "./invalid_data_output.json"
    expected_output_path = "./invalid_data_output.json"
    actual_output_path = task_func(data, output_path)
    assert actual_output_path == expected_output_path
    with open(actual_output_path, "r") as file:
        data_dict = json.load(file)
    expected_data_dict = {"a": [1, 2, 3], "b": [4, 5, 6]}
    assert data_dict == expected_data_dict