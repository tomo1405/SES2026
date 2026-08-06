import numpy as np
import pandas as pd
import pytest
from src_0219 import task_func


# Mock data for testing
def create_mock_df():
    data = {
        'feature1': [1, 2, 3],
        'feature2': [4, 5, 6],
        'feature3': [7, 8, 9],
        'feature4': [10, 11, 12],
        'feature5': [13, 14, 15],
        'target': [16, 17, 18]
    }
    return pd.DataFrame(data)

# Test cases
def test_task_func_input_type():
    df = create_mock_df()
    dict_mapping = {'feature1': {1: 0}}
    result_df, _ = task_func(df, dict_mapping)
    assert isinstance(result_df, pd.DataFrame)

def test_task_func_missing_columns():
    df = create_mock_df().drop(columns=['feature1'])
    dict_mapping = {'feature1': {1: 0}}
    with pytest.raises(ValueError, match="Missing columns in DataFrame:"):
        task_func(df, dict_mapping)

def test_task_func_value_replacement():
    df = create_mock_df()
    dict_mapping = {'feature1': {1: 0}}
    result_df, _ = task_func(df, dict_mapping)
    assert result_df['feature1'].equals(pd.Series([0, 2, 3]))

def test_task_func_feature_standardization():
    df = create_mock_df()
    dict_mapping = {}
    result_df, _ = task_func(df, dict_mapping)
    assert np.allclose(result_df[FEATURES].mean(), 0, atol=1e-7)
    assert np.allclose(result_df[FEATURES].std(), 1, atol=1e-7)

def test_task_func_plot_histogram():
    df = create_mock_df()
    dict_mapping = {}
    result_df, ax = task_func(df, dict_mapping, plot_histogram=True)
    assert isinstance(ax, pd.Series)

def test_task_func_no_plot_histogram():
    df = create_mock_df()
    dict_mapping = {}
    result_df, ax = task_func(df, dict_mapping, plot_histogram=False)
    assert ax is None