import pytest
from src_0412 import task_func
import os
import pandas as pd
import json

@pytest.fixture
def sample_data():
    return {
        "a": [1, 2, 3],
        "b": [4, 5, 6],
        "c": [7, 8, 9]
    }

@pytest.fixture
def expected_json(sample_data):
    df = pd.DataFrame(sample_data).drop(columns="c", errors="ignore")
    return df.to_dict(orient="dict")

def test_task_func_with_column_c(sample_data, expected_json, tmpdir):
    output_path = str(tmpdir / "test_output.json")
    result_path = task_func(sample_data, output_path)
    assert result_path == output_path
    with open(output_path, "r") as file:
        actual_json = json.load(file)
    assert actual_json == expected_json

def test_task_func_without_column_c(tmpdir):
    sample_data = {
        "a": [1, 2, 3],
        "b": [4, 5, 6]
    }
    expected_json = {
        "a": {0: 1, 1: 2, 2: 3},
        "b": {0: 4, 1: 5, 2: 6}
    }
    output_path = str(tmpdir / "test_output.json")
    result_path = task_func(sample_data, output_path)
    assert result_path == output_path
    with open(output_path, "r") as file:
        actual_json = json.load(file)
    assert actual_json == expected_json

def test_task_func_default_output_path(sample_data, expected_json, tmpdir):
    output_path = "./default_data_output.json"
    result_path = task_func(sample_data)
    assert result_path == output_path
    with open(output_path, "r") as file:
        actual_json = json.load(file)
    assert actual_json == expected_json
    os.remove(output_path)  # Clean up the default output file

def test_task_func_empty_data(tmpdir):
    sample_data = {}
    expected_json = {}
    output_path = str(tmpdir / "test_output.json")
    result_path = task_func(sample_data, output_path)
    assert result_path == output_path
    with open(output_path, "r") as file:
        actual_json = json.load(file)
    assert actual_json == expected_json