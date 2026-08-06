import pytest
from src_0527 import task_func
import json
import pandas as pd
import numpy as np

# Mocking the file reading for testing
@pytest.fixture
def mock_json_data(tmp_path):
    data = [
        {"a": 1, "b": 2.5},
        {"a": 3, "b": 4.5, "c": "string"},
        {"a": 5, "c": "another string"}
    ]
    json_file = tmp_path / "data.json"
    with open(json_file, "w") as f:
        json.dump(data, f)
    return json_file

def test_task_func_with_valid_data(mock_json_data):
    df = task_func(str(mock_json_data))
    expected_columns = ['mean', 'median']
    assert list(df.columns) == expected_columns
    assert len(df) == 3  # There are 3 unique keys across all entries: 'a', 'b', and 'c'
    assert df.loc['a']['mean'] == 3.0
    assert df.loc['a']['median'] == 3.0
    assert np.isnan(df.loc['b']['mean'])
    assert np.isnan(df.loc['b']['median'])
    assert np.isnan(df.loc['c']['mean'])
    assert np.isnan(df.loc['c']['median'])

def test_task_func_with_empty_file(tmp_path):
    json_file = tmp_path / "empty_data.json"
    with open(json_file, "w") as f:
        json.dump([], f)
    df = task_func(str(json_file))
    assert df.empty

def test_task_func_with_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        task_func("nonexistent_file.json")

def test_task_func_with_invalid_json(tmp_path):
    json_file = tmp_path / "invalid_data.json"
    with open(json_file, "w") as f:
        f.write("{invalid json}")
    with pytest.raises(json.JSONDecodeError):
        task_func(str(json_file))