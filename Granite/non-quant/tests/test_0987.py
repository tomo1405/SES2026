import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from src_0987 import task_func

def test_task_func():
    json_data = '{"key1": {"key2": [1, 2, 3, 4, 5]}}'
    key_path = ["key1", "key2"]
    expected_values = np.array([1, 2, 3, 4, 5])
    expected_df = pd.DataFrame({"Values": expected_values})
    expected_fig, expected_ax = plt.subplots()
    sns.boxplot(data=expected_df, ax=expected_ax)

    actual_fig = task_func(json_data, key_path)

    assert actual_fig == expected_fig

def test_task_func_json_decode_error():
    json_data = '{"key1": {"key2": [1, 2, 3, 4, 5]}'
    key_path = ["key1", "key2"]

    try:
        task_func(json_data, key_path)
        assert False, "Expected JSONDecodeError was not raised"
    except ValueError as e:
        assert "Input malformed" in str(e)

def test_task_func_key_error():
    json_data = '{"key1": {"key2": [1, 2, 3, 4, 5]}}'
    key_path = ["key1", "key3"]

    try:
        task_func(json_data, key_path)
        assert False, "Expected KeyError was not raised"
    except KeyError as e:
        assert "Key error occurred" in str(e)

def test_task_func_value_error():
    json_data = '{"key1": {"key2": []}}'
    key_path = ["key1", "key2"]

    try:
        task_func(json_data, key_path)
        assert False, "Expected ValueError was not raised"
    except ValueError as e:
        assert "Value error occurred" in str(e)