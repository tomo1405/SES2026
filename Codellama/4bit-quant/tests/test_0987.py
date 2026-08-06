import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest
import seaborn as sns
from src_0987 import task_func


def test_task_func():
    # Test case 1: Valid JSON data and valid key path
    json_data = '{"key1": {"key2": [1, 2, 3]}}'
    key_path = ["key1", "key2"]
    expected_values = np.array([1, 2, 3])
    expected_df = pd.DataFrame(expected_values, columns=["Values"])
    expected_fig = plt.figure()
    sns.boxplot(data=expected_df, ax=expected_fig.axes[0])

    fig = task_func(json_data, key_path)
    assert fig == expected_fig

    # Test case 2: Invalid JSON data
    json_data = '{"key1": {"key2": [1, 2, 3]}'
    key_path = ["key1", "key2"]

    with pytest.raises(ValueError):
        task_func(json_data, key_path)

    # Test case 3: Invalid key path
    json_data = '{"key1": {"key2": [1, 2, 3]}}'
    key_path = ["key1", "key3"]

    with pytest.raises(KeyError):
        task_func(json_data, key_path)

    # Test case 4: Empty data string
    json_data = '{"key1": {"key2": []}}'
    key_path = ["key1", "key2"]

    with pytest.raises(ValueError):
        task_func(json_data, key_path)

    # Test case 5: No numeric data found
    json_data = '{"key1": {"key2": ["a", "b", "c"]}}'
    key_path = ["key1", "key2"]

    with pytest.raises(ValueError):
        task_func(json_data, key_path)