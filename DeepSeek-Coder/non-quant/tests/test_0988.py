import pytest
from src_0988 import task_func
import json
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Test cases for task_func

def test_task_func_basic():
    json_data = '{"key1": {"key2": [1, 2, 3, 4, 5]}'
    data_key = "key1.key2"
    values, normalized_values, ax = task_func(json_data, data_key)
    assert isinstance(values, pd.Series)
    assert isinstance(normalized_values, pd.Series)
    assert ax is not None
    assert len(ax.get_lines()) == 2  # Check if two plots are plotted

def test_task_func_empty():
    json_data = '{"key1": {}}'
    data_key = "key1"
    with pytest.raises(KeyError):
        task_func(json_data, data_key)

def test_task_func_empty_data():
    json_data = '{"key1": {}}'
    data_key = "key1"
    values, normalized_values, ax = task_func(json_data, data_key)
    assert values.empty
    assert normalized_values is None
    assert ax is None