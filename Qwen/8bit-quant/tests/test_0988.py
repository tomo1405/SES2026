import pytest
from src_0988 import task_func
import json
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def test_task_func_valid_json():
    json_data = '{"a": {"b": [1.0, 2.0, 3.0]}}'
    data_key = "a.b"
    original, normalized, ax = task_func(json_data, data_key)
    
    assert isinstance(original, pd.Series)
    assert isinstance(normalized, pd.Series)
    assert isinstance(ax, plt.Axes)
    
    pd.testing.assert_series_equal(original, pd.Series([1.0, 2.0, 3.0], dtype='Float64'))
    pd.testing.assert_series_equal(normalized, pd.Series([0.0, 0.5, 1.0], dtype='Float64'))

def test_task_func_empty_json():
    json_data = '{"a": {"b": []}}'
    data_key = "a.b"
    original, normalized, ax = task_func(json_data, data_key)
    
    assert isinstance(original, pd.Series)
    assert isinstance(normalized, pd.Series)
    assert isinstance(ax, plt.Axes)
    
    assert original.empty
    assert normalized.empty

def test_task_func_invalid_key_path():
    json_data = '{"a": {"b": [1.0, 2.0, 3.0]}}'
    data_key = "a.c"
    
    with pytest.raises(KeyError) as excinfo:
        task_func(json_data, data_key)
    
    assert str(excinfo.value) == "Key path 'a.c' not found in the provided JSON data."

def test_task_func_non_numeric_data():
    json_data = '{"a": {"b": ["one", "two", "three"]}}'
    data_key = "a.b"
    
    with pytest.raises(ValueError) as excinfo:
        task_func(json_data, data_key)
    
    assert str(excinfo.value) == "could not convert string to float: 'one'"