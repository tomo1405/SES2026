import json
import os

import pandas as pd
import pytest
from src_0412 import task_func


def test_task_func():
    data = {"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]}
    output_path = "./test_data_output.json"
    expected_output_path = "./test_data_output.json"
    df = pd.DataFrame(data)
    df = df.drop(columns="c", errors="ignore")
    data_dict = df.to_dict(orient="dict")
    with open(output_path, "w") as file:
        json.dump(data_dict, file)
    assert task_func(data, output_path) == expected_output_path
    assert os.path.exists(output_path)
    with open(output_path, "r") as file:
        data_dict = json.load(file)
    assert data_dict == {"a": [1, 2, 3], "b": [4, 5, 6]}
    os.remove(output_path)

def test_task_func_with_output_path():
    data = {"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]}
    output_path = "./test_data_output.json"
    expected_output_path = "./test_data_output.json"
    df = pd.DataFrame(data)
    df = df.drop(columns="c", errors="ignore")
    data_dict = df.to_dict(orient="dict")
    with open(output_path, "w") as file:
        json.dump(data_dict, file)
    assert task_func(data, output_path) == expected_output_path
    assert os.path.exists(output_path)
    with open(output_path, "r") as file:
        data_dict = json.load(file)
    assert data_dict == {"a": [1, 2, 3], "b": [4, 5, 6]}
    os.remove(output_path)

def test_task_func_with_invalid_data():
    with pytest.raises(TypeError):
        task_func("invalid_data", "./test_data_output.json")

def test_task_func_with_invalid_output_path():
    with pytest.raises(TypeError):
        task_func({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]}, 123)