import pytest
from src_0987 import task_func
import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def test_task_func_valid_input():
    json_data = '{"key1": [1, 2, 3], "key2": [4, 5, 6]}'
    key_path = ["key1", "key2"]
    expected_values = np.array([1, 2, 3, 4, 5, 6])

    fig = task_func(json_data, key_path)
    assert isinstance(fig, plt.Figure)

    df = pd.DataFrame(expected_values, columns=["Values"])
    sns.boxplot(data=df, ax=fig.axes[0])

    assert np.array_equal(fig.axes[0].get_xlabel(), "Values")
    assert np.array_equal(fig.axes[0].get_ylabel(), "Count")

def test_task_func_invalid_input():
    json_data = '{"key1": [1, 2, 3], "key2": [4, 5, 6]}'
    key_path = ["key1", "key3"]

    with pytest.raises(KeyError):
        task_func(json_data, key_path)

def test_task_func_empty_input():
    json_data = '{"key1": [1, 2, 3], "key2": [4, 5, 6]}'
    key_path = []

    with pytest.raises(ValueError):
        task_func(json_data, key_path)

def test_task_func_malformed_input():
    json_data = '{"key1": [1, 2, 3], "key2": [4, 5, 6]}'
    key_path = ["key1", "key2"]

    with pytest.raises(json.decoder.JSONDecodeError):
        task_func(json_data, key_path)