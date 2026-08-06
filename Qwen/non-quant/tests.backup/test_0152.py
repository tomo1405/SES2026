import pytest
from src_0152 import task_func
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def test_task_func_no_matching_keys():
    data_dict = {'a': [1, 2, 3], 'b': [4, 5, 6]}
    data_keys = ['c', 'd']
    with pytest.raises(ValueError) as excinfo:
        task_func(data_dict, data_keys)
    assert str(excinfo.value) == "No matching keys found in data dictionary, or keys list is empty."

def test_task_func_empty_keys_list():
    data_dict = {'a': [1, 2, 3], 'b': [4, 5, 6]}
    data_keys = []
    with pytest.raises(ValueError) as excinfo:
        task_func(data_dict, data_keys)
    assert str(excinfo.value) == "No matching keys found in data dictionary, or keys list is empty."

def test_task_func_valid_data():
    data_dict = {'a': [1, 2, 3], 'b': [4, 5, 6]}
    data_keys = ['a', 'b']
    normalized_df, ax = task_func(data_dict, data_keys)
    
    # Check if the returned DataFrame is not empty
    assert not normalized_df.empty
    
    # Check if the DataFrame has the correct shape
    assert normalized_df.shape == (3, 2)
    
    # Check if the DataFrame columns are correct
    assert list(normalized_df.columns) == data_keys
    
    # Check if the values are normalized between 0 and 1
    scaler = MinMaxScaler()
    expected_normalized_data = scaler.fit_transform(pd.DataFrame(data_dict[data_keys]))
    expected_normalized_df = pd.DataFrame(expected_normalized_data, columns=data_keys)
    pd.testing.assert_frame_equal(normalized_df, expected_normalized_df)

def test_task_func_single_key():
    data_dict = {'a': [1, 2, 3], 'b': [4, 5, 6]}
    data_keys = ['a']
    normalized_df, ax = task_func(data_dict, data_keys)
    
    # Check if the returned DataFrame is not empty
    assert not normalized_df.empty
    
    # Check if the DataFrame has the correct shape
    assert normalized_df.shape == (3, 1)
    
    # Check if the DataFrame columns are correct
    assert list(normalized_df.columns) == data_keys
    
    # Check if the values are normalized between 0 and 1
    scaler = MinMaxScaler()
    expected_normalized_data = scaler.fit_transform(pd.DataFrame(data_dict[data_keys]))
    expected_normalized_df = pd.DataFrame(expected_normalized_data, columns=data_keys)
    pd.testing.assert_frame_equal(normalized_df, expected_normalized_df)