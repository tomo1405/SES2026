import pytest
from src_0152 import task_func
import pandas as pd
import numpy as np

def test_task_func_with_valid_data():
    data_dict = {
        'feature1': [1, 2, 3],
        'feature2': [4, 5, 6],
        'feature3': [7, 8, 9]
    }
    data_keys = ['feature1', 'feature2']

    normalized_df, ax = task_func(data_dict, data_keys)

    assert isinstance(normalized_df, pd.DataFrame)
    assert all(key in normalized_df.columns for key in data_keys)
    assert normalized_df.shape == (3, 2)  # 3 rows for each feature, 2 columns for the two features
    assert ax.get_title() == 'Normalized Data'
    assert ax.get_ylabel() == 'Normalized Value'
    assert ax.get_xlabel() == 'Index'

def test_task_func_with_no_matching_keys():
    data_dict = {
        'feature1': [1, 2, 3],
        'feature2': [4, 5, 6]
    }
    data_keys = ['feature3', 'feature4']

    with pytest.raises(ValueError, match="No matching keys found in data dictionary, or keys list is empty."):
        task_func(data_dict, data_keys)

def test_task_func_with_empty_keys_list():
    data_dict = {
        'feature1': [1, 2, 3],
        'feature2': [4, 5, 6]
    }
    data_keys = []

    with pytest.raises(ValueError, match="No matching keys found in data dictionary, or keys list is empty."):
        task_func(data_dict, data_keys)

def test_task_func_with_single_key():
    data_dict = {
        'feature1': [1, 2, 3],
        'feature2': [4, 5, 6]
    }
    data_keys = ['feature1']

    normalized_df, ax = task_func(data_dict, data_keys)

    assert isinstance(normalized_df, pd.DataFrame)
    assert all(key in normalized_df.columns for key in data_keys)
    assert normalized_df.shape == (3, 1)  # 3 rows for each feature, 1 column for the one feature
    assert ax.get_title() == 'Normalized Data'
    assert ax.get_ylabel() == 'Normalized Value'
    assert ax.get_xlabel() == 'Index'