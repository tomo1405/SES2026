import matplotlib.pyplot as plt
import pandas as pd
import pytest
from sklearn.preprocessing import StandardScaler
from src_0219 import task_func

# Constants
FEATURES = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']
TARGET = 'target'

def test_task_func_input_type():
    with pytest.raises(ValueError, match="Input df is not a DataFrame."):
        task_func([1, 2, 3], {})

def test_task_func_missing_columns():
    data = {
        'feature1': [1, 2, 3],
        'feature2': [4, 5, 6],
        'feature3': [7, 8, 9],
        'feature4': [10, 11, 12]
    }
    df = pd.DataFrame(data)
    dict_mapping = {}
    with pytest.raises(ValueError, match="Missing columns in DataFrame: \['target'\]"):
        task_func(df, dict_mapping)

def test_task_func_replace_values():
    data = {
        'feature1': [1, 2, 3],
        'feature2': [4, 5, 6],
        'feature3': [7, 8, 9],
        'feature4': [10, 11, 12],
        'feature5': [13, 14, 15],
        'target': [16, 17, 18]
    }
    df = pd.DataFrame(data)
    dict_mapping = {'feature1': {1: 100}}
    expected_df = df.copy()
    expected_df['feature1'] = [100, 2, 3]
    result_df, _ = task_func(df, dict_mapping)
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_standardization():
    data = {
        'feature1': [1, 2, 3],
        'feature2': [4, 5, 6],
        'feature3': [7, 8, 9],
        'feature4': [10, 11, 12],
        'feature5': [13, 14, 15],
        'target': [16, 17, 18]
    }
    df = pd.DataFrame(data)
    dict_mapping = {}
    result_df, _ = task_func(df, dict_mapping)
    scaler = StandardScaler()
    expected_features = scaler.fit_transform(df[FEATURES])
    pd.testing.assert_frame_equal(result_df[FEATURES], pd.DataFrame(expected_features, columns=FEATURES))

def test_task_func_plot_histogram():
    data = {
        'feature1': [1, 2, 3],
        'feature2': [4, 5, 6],
        'feature3': [7, 8, 9],
        'feature4': [10, 11, 12],
        'feature5': [13, 14, 15],
        'target': [16, 17, 18]
    }
    df = pd.DataFrame(data)
    dict_mapping = {}
    result_df, ax = task_func(df, dict_mapping, plot_histogram=True)
    assert ax is not None
    assert isinstance(ax, plt.Axes)

def test_task_func_no_plot_histogram():
    data = {
        'feature1': [1, 2, 3],
        'feature2': [4, 5, 6],
        'feature3': [7, 8, 9],
        'feature4': [10, 11, 12],
        'feature5': [13, 14, 15],
        'target': [16, 17, 18]
    }
    df = pd.DataFrame(data)
    dict_mapping = {}
    result_df, ax = task_func(df, dict_mapping, plot_histogram=False)
    assert ax is None