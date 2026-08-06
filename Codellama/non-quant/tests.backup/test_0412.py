import pytest
from src_0412 import task_func
import pandas as pd
import json

def test_task_func():
    # Test case 1: Test with a valid dictionary
    data = {"a": [1, 2, 3], "b": [4, 5, 6]}
    output_path = "./test_data_output.json"
    expected_output = {"a": [1, 2, 3], "b": [4, 5, 6]}
    actual_output = task_func(data, output_path)
    assert actual_output == output_path
    with open(output_path, "r") as file:
        actual_data = json.load(file)
    assert actual_data == expected_output

    # Test case 2: Test with a dictionary with a column named 'c'
    data = {"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]}
    output_path = "./test_data_output.json"
    expected_output = {"a": [1, 2, 3], "b": [4, 5, 6]}
    actual_output = task_func(data, output_path)
    assert actual_output == output_path
    with open(output_path, "r") as file:
        actual_data = json.load(file)
    assert actual_data == expected_output

    # Test case 3: Test with a dictionary with a column named 'c' and a different output path
    data = {"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]}
    output_path = "./test_data_output_2.json"
    expected_output = {"a": [1, 2, 3], "b": [4, 5, 6]}
    actual_output = task_func(data, output_path)
    assert actual_output == output_path
    with open(output_path, "r") as file:
        actual_data = json.load(file)
    assert actual_data == expected_output