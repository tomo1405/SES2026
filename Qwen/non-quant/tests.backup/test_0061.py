import pytest
from src_0061 import task_func
import os
import pandas as pd
import json

def test_task_func_with_default_paths(tmpdir):
    result = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
    csv_file_path = str(tmpdir.join("test.csv"))
    json_file_path = str(tmpdir.join("test.json"))

    task_func(result, csv_file_path, json_file_path)

    # Check CSV file
    df = pd.read_csv(csv_file_path)
    assert df.equals(pd.DataFrame(result))

    # Check JSON file
    with open(json_file_path, 'r') as f:
        loaded_data = json.load(f)
    assert loaded_data == result

def test_task_func_with_custom_paths(tmpdir):
    result = [{"name": "Charlie", "age": 35}, {"name": "David", "age": 40}]
    csv_file_path = str(tmpdir.join("custom_test.csv"))
    json_file_path = str(tmpdir.join("custom_test.json"))

    task_func(result, csv_file_path, json_file_path)

    # Check CSV file
    df = pd.read_csv(csv_file_path)
    assert df.equals(pd.DataFrame(result))

    # Check JSON file
    with open(json_file_path, 'r') as f:
        loaded_data = json.load(f)
    assert loaded_data == result

def test_task_func_no_data(tmpdir):
    result = []
    csv_file_path = str(tmpdir.join("empty_test.csv"))
    json_file_path = str(tmpdir.join("empty_test.json"))

    task_func(result, csv_file_path, json_file_path)

    # Check CSV file
    df = pd.read_csv(csv_file_path)
    assert df.equals(pd.DataFrame(result))

    # Check JSON file
    with open(json_file_path, 'r') as f:
        loaded_data = json.load(f)
    assert loaded_data == result