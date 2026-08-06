import json
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import pytest

def task_func(json_data: str, data_key: str):
    data = json.loads(json_data)
    try:
        data = json.loads(json_data)
        for key in data_key.split("."):
            data = data[key]
        values = pd.Series(data, dtype=pd.Float64Dtype)
    except KeyError:
        raise KeyError(f"Key path '{data_key}' not found in the provided JSON data.")

    if values.empty:
        return values, None, None

    scaler = MinMaxScaler()
    normalized_values = pd.Series(
        scaler.fit_transform(values.values.reshape(-1, 1)).flatten(),
        dtype=pd.Float64Dtype,
    )

    fig, ax = plt.subplots()
    ax.plot(values, label="Original Data")
    ax.plot(normalized_values, label="Normalized Data")
    ax.set_title("Comparison of Original and Normalized Data")
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    ax.legend()

    return values, normalized_values, ax

def test_task_func():
    json_data = '{"a": 1, "b": 2, "c": 3}'
    data_key = "a"
    expected_values = pd.Series([1], dtype=pd.Float64Dtype)
    expected_normalized_values = pd.Series([0.0], dtype=pd.Float64Dtype)
    expected_ax = None
    values, normalized_values, ax = task_func(json_data, data_key)
    assert values.equals(expected_values)
    assert normalized_values.equals(expected_normalized_values)
    assert ax is expected_ax

def test_task_func_with_empty_values():
    json_data = '[{"a": 1}, {"a": 2}, {"a": 3}]'
    data_key = "a"
    expected_values = pd.Series([], dtype=pd.Float64Dtype)
    expected_normalized_values = pd.Series([], dtype=pd.Float64Dtype)
    expected_ax = None
    values, normalized_values, ax = task_func(json_data, data_key)
    assert values.equals(expected_values)
    assert normalized_values.equals(expected_normalized_values)
    assert ax is expected_ax

def test_task_func_with_invalid_json_data():
    json_data = '{"a": 1, "b": 2, "c": 3'
    data_key = "a"
    with pytest.raises(ValueError):
        task_func(json_data, data_key)

def test_task_func_with_invalid_data_key():
    json_data = '{"a": 1, "b": 2, "c": 3}'
    data_key = "d"
    with pytest.raises(KeyError):
        task_func(json_data, data_key)