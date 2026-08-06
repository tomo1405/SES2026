import pytest
from src_0987 import task_func
import json
import numpy as np
import pandas as pd
import io
import matplotlib.pyplot as plt

def test_task_func_valid_json():
    json_data = '{"data": "1,2,3,4,5"}'
    key_path = ["data"]
    fig = task_func(json_data, key_path)
    assert isinstance(fig, plt.Figure)
    plt.close(fig)

def test_task_func_invalid_json():
    json_data = '{"data": "1,2,3,4,5"'
    key_path = ["data"]
    with pytest.raises(ValueError) as excinfo:
        task_func(json_data, key_path)
    assert "Input malformed" in str(excinfo.value)

def test_task_func_missing_key():
    json_data = '{"data": "1,2,3,4,5"}'
    key_path = ["missing_key"]
    with pytest.raises(KeyError) as excinfo:
        task_func(json_data, key_path)
    assert "Key error occurred" in str(excinfo.value)

def test_task_func_empty_data_string():
    json_data = '{"data": ""}'
    key_path = ["data"]
    with pytest.raises(ValueError) as excinfo:
        task_func(json_data, key_path)
    assert "No numeric data found or empty data string" in str(excinfo.value)

def test_task_func_non_numeric_data():
    json_data = '{"data": "a,b,c,d,e"}'
    key_path = ["data"]
    with pytest.raises(ValueError) as excinfo:
        task_func(json_data, key_path)
    assert "could not convert string to float" in str(excinfo.value)

def test_task_func_correct_values():
    json_data = '{"data": "1,2,3,4,5"}'
    key_path = ["data"]
    fig = task_func(json_data, key_path)
    expected_values = np.array([1, 2, 3, 4, 5])
    df = pd.read_csv(io.StringIO(json_data.split('"')[1]), header=None, names=["Values"])
    assert np.array_equal(df["Values"], expected_values)
    plt.close(fig)