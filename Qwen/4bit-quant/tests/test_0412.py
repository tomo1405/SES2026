import pytest
from src_0412 import task_func
import os
import pandas as pd
import json

def test_task_func_with_default_path():
    data = {"a": [1, 2], "b": [3, 4]}
    output_path = task_func(data)
    assert os.path.exists(output_path)
    with open(output_path, "r") as file:
        content = json.load(file)
    expected_content = {"a": {0: 1, 1: 2}, "b": {0: 3, 1: 4}}
    assert content == expected_content
    os.remove(output_path)

def test_task_func_with_custom_path():
    data = {"a": [1, 2], "b": [3, 4]}
    custom_path = "./custom_data_output.json"
    output_path = task_func(data, custom_path)
    assert os.path.exists(output_path)
    with open(output_path, "r") as file:
        content = json.load(file)
    expected_content = {"a": {0: 1, 1: 2}, "b": {0: 3, 1: 4}}
    assert content == expected_content
    os.remove(custom_path)

def test_task_func_with_column_c():
    data = {"a": [1, 2], "b": [3, 4], "c": [5, 6]}
    output_path = task_func(data)
    assert os.path.exists(output_path)
    with open(output_path, "r") as file:
        content = json.load(file)
    expected_content = {"a": {0: 1, 1: 2}, "b": {0: 3, 1: 4}}
    assert content == expected_content
    os.remove(output_path)

def test_task_func_with_empty_data():
    data = {}
    output_path = task_func(data)
    assert os.path.exists(output_path)
    with open(output_path, "r") as file:
        content = json.load(file)
    expected_content = {}
    assert content == expected_content
    os.remove(output_path)

def test_task_func_with_single_row():
    data = {"a": [1], "b": [3]}
    output_path = task_func(data)
    assert os.path.exists(output_path)
    with open(output_path, "r") as file:
        content = json.load(file)
    expected_content = {"a": {0: 1}, "b": {0: 3}}
    assert content == expected_content
    os.remove(output_path)