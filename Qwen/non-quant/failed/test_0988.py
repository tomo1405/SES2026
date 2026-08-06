import pytest
from src_0988 import task_func
import json
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

# Mocking plt.show to avoid displaying plots during tests
plt.show = lambda: None

def test_task_func_valid_json():
    json_data = '{"key1": {"key2": [1, 2, 3, 4, 5]}}'
    data_key = "key1.key2"
    original, normalized, ax = task_func(json_data, data_key)
    
    assert isinstance(original, pd.Series)
    assert isinstance(normalized, pd.Series)
    assert isinstance(ax, plt.Axes)
    
    assert all(original == pd.Series([1, 2, 3, 4, 5], dtype=pd.Float64Dtype))
    assert all(normalized == pd.Series([0.0, 0.25, 0.5, 0.75, 1.0], dtype=pd.Float64Dtype))

def test_task_func_empty_data():
    json_data = '{"key1": {"key2": []}}'
    data_key = "key1.key2"
    original, normalized, ax = task_func(json_data, data_key)
    
    assert isinstance(original, pd.Series)
    assert isinstance(normalized, pd.Series)
    assert isinstance(ax, plt.Axes)
    
    assert original.empty
    assert normalized.empty

def test_task_func_invalid_key_path():
    json_data = '{"key1": {"key2": [1, 2, 3, 4, 5]}}'
    data_key = "key1.key3"
    
    with pytest.raises(KeyError) as excinfo:
        task_func(json_data, data_key)
    
    assert str(excinfo.value) == "Key path 'key1.key3' not found in the provided JSON data."

def test_task_func_non_numeric_data():
    json_data = '{"key1": {"key2": ["a", "b", "c"]}}'
    data_key = "key1.key2"
    
    with pytest.raises(ValueError) as excinfo:
        task_func(json_data, data_key)
    
    assert str(excinfo.value).startswith("could not convert string to float")

def test_task_func_single_value():
    json_data = '{"key1": {"key2": [10]}}'
    data_key = "key1.key2"
    original, normalized, ax = task_func(json_data, data_key)
    
    assert isinstance(original, pd.Series)
    assert isinstance(normalized, pd.Series)
    assert isinstance(ax, plt.Axes)
    
    assert all(original == pd.Series([10], dtype=pd.Float64Dtype))
    assert all(normalized == pd.Series([0.0], dtype=pd.Float64Dtype))