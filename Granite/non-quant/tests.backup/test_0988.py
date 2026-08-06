import json
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from unittest.mock import patch

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
    json_data = '{"a": {"b": 1.2}, "c": 3.4}'
    data_key = "a.b"
    values, normalized_values, ax = task_func(json_data, data_key)
    assert isinstance(values, pd.Series)
    assert isinstance(normalized_values, pd.Series)
    assert isinstance(ax, plt.Axes)

def test_task_func_empty_data():
    json_data = '{"a": {"b": []}, "c": 3.4}'
    data_key = "a.b"
    values, normalized_values, ax = task_func(json_data, data_key)
    assert isinstance(values, pd.Series)
    assert normalized_values is None
    assert ax is None

@patch("matplotlib.pyplot.show")
def test_task_func_plot(mock_show):
    json_data = '{"a": {"b": 1.2}, "c": 3.4}'
    data_key = "a.b"
    values, normalized_values, ax = task_func(json_data, data_key)
    assert isinstance(ax, plt.Axes)
    ax.legend.assert_called_once()
    mock_show.assert_called_once()