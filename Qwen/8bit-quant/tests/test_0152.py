import pytest
from src_0152 import task_func
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def test_task_func_empty_keys():
    data_dict = {'a': [1, 2, 3], 'b': [4, 5, 6]}
    data_keys = []
    with pytest.raises(ValueError) as excinfo:
        task_func(data_dict, data_keys)
    assert str(excinfo.value) == "No matching keys found in data dictionary, or keys list is empty."

def test_task_func_no_matching_keys():
    data_dict = {'a': [1, 2, 3], 'b': [4, 5, 6]}
    data_keys = ['c', 'd']
    with pytest.raises(ValueError) as excinfo:
        task_func(data_dict, data_keys)
    assert str(excinfo.value) == "No matching keys found in data dictionary, or keys list is empty."

def test_task_func_single_key():
    data_dict = {'a': [1, 2, 3], 'b': [4, 5, 6]}
    data_keys = ['a']
    normalized_df, ax = task_func(data_dict, data_keys)
    expected_df = pd.DataFrame({'a': [0.0, 0.5, 1.0]})
    pd.testing.assert_frame_equal(normalized_df, expected_df)
    assert isinstance(ax, pd.core.series.Series)

def test_task_func_multiple_keys():
    data_dict = {'a': [1, 2, 3], 'b': [4, 5, 6]}
    data_keys = ['a', 'b']
    normalized_df, ax = task_func(data_dict, data_keys)
    expected_df = pd.DataFrame({'a': [0.0, 0.5, 1.0], 'b': [0.0, 0.5, 1.0]})
    pd.testing.assert_frame_equal(normalized_df, expected_df)
    assert isinstance(ax, pd.core.series.Series)

def test_task_func_with_negative_values():
    data_dict = {'a': [-1, 0, 1], 'b': [-2, 0, 2]}
    data_keys = ['a', 'b']
    normalized_df, ax = task_func(data_dict, data_keys)
    expected_df = pd.DataFrame({'a': [0.0, 0.5, 1.0], 'b': [0.0, 0.5, 1.0]})
    pd.testing.assert_frame_equal(normalized_df, expected_df)
    assert isinstance(ax, pd.core.series.Series)

def test_task_func_with_all_same_values():
    data_dict = {'a': [5, 5, 5], 'b': [10, 10, 10]}
    data_keys = ['a', 'b']
    with pytest.raises(ValueError) as excinfo:
        task_func(data_dict, data_keys)
    assert str(excinfo.value) == "Data contains constant values which cannot be normalized."