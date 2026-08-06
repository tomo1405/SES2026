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
    assert np.array_equal(df.values, fig.data)

def test_task_func_invalid_json():
    json_data = '{"key1": [1, 2, 3], "key2": [4, 5, 6]'
    key_path = ["key1", "key2"]

    with pytest.raises(ValueError) as e:
        task_func(json_data, key_path)

    assert "Input malformed" in str(e.value)

def test_task_func_invalid_key_path():
    json_data = '{"key1": [1, 2, 3], "key2": [4, 5, 6]}'
    key_path = ["key1", "key3"]

    with pytest.raises(KeyError) as e:
        task_func(json_data, key_path)

    assert "Key error occurred" in str(e.value)

def test_task_func_empty_data():
    json_data = '{"key1": [], "key2": []}'
    key_path = ["key1", "key2"]

    with pytest.raises(ValueError) as e:
        task_func(json_data, key_path)

    assert "No numeric data found or empty data string." in str(e.value)