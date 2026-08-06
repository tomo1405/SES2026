python
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
    # Test case 1: Valid JSON data and valid key path
    json_data = '{"name": "John", "age": 30, "city": {"name": "New York", "population": 8399000}}'
    data_key = "city.population"
    expected_values = pd.Series([8399000], dtype=pd.Float64Dtype)
    expected_normalized_values = pd.Series([1.0], dtype=pd.Float64Dtype)
    expected_ax = None
    values, normalized_values, ax = task_func(json_data, data_key)
    assert values.equals(expected_values)
    assert normalized_values.equals(expected_normalized_values)
    assert ax == expected_ax

    # Test case 2: Valid JSON data and invalid key path
    json_data = '{"name": "John", "age": 30, "city": {"name": "New York", "population": 8399000}}'
    data_key = "city.population.invalid"
    with pytest.raises(KeyError):
        task_func(json_data, data_key)

    # Test case 3: Invalid JSON data
    json_data = '{"name": "John", "age": 30, "city": {"name": "New York", "population": 8399000}'
    data_key = "city.population"
    with pytest.raises(json.JSONDecodeError):
        task_func(json_data, data_key)

    # Test case 4: Empty JSON data
    json_data = ""
    data_key = "city.population"
    with pytest.raises(json.JSONDecodeError):
        task_func(json_data, data_key)

    # Test case 5: Empty key path
    json_data = '{"name": "John", "age": 30, "city": {"name": "New York", "population": 8399000}}'
    data_key = ""
    with pytest.raises(KeyError):
        task_func(json_data, data_key)

    # Test case 6: Empty values
    json_data = '{"name": "John", "age": 30, "city": {"name": "New York", "population": 8399000}}'
    data_key = "city.population"
    expected_values = pd.Series([], dtype=pd.Float64Dtype)
    expected_normalized_values = pd.Series([], dtype=pd.Float64Dtype)
    expected_ax = None
    values, normalized_values, ax = task_func(json_data, data_key)
    assert values.equals(expected_values)
    assert normalized_values.equals(expected_normalized_values)
    assert ax == expected_ax