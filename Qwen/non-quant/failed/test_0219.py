import pytest
from src_0219 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_df():
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'feature3': [2, 3, 4, 5, 6],
        'feature4': [6, 5, 4, 3, 2],
        'feature5': [3, 4, 5, 6, 7],
        'target': [10, 20, 30, 40, 50]
    }
    return pd.DataFrame(data)

@pytest.fixture
def dict_mapping():
    return {'feature1': {1: 10, 2: 20}, 'target': {10: 100, 20: 200}}

def test_task_func_input_type(sample_df, dict_mapping):
    with pytest.raises(ValueError, match="Input df is not a DataFrame."):
        task_func([1, 2, 3], dict_mapping)

def test_task_func_missing_columns(sample_df, dict_mapping):
    sample_df = sample_df.drop(columns=['feature1'])
    with pytest.raises(ValueError, match="Missing columns in DataFrame: \['feature1'\]"):
        task_func(sample_df, dict_mapping)

def test_task_func_value_replacement(sample_df, dict_mapping):
    result_df, _ = task_func(sample_df, dict_mapping)
    assert result_df.loc[0, 'feature1'] == 10
    assert result_df.loc[0, 'target'] == 100

def test_task_func_feature_standardization(sample_df, dict_mapping):
    result_df, _ = task_func(sample_df, dict_mapping)
    np.testing.assert_array_almost_equal(result_df[FEATURES].mean(), np.zeros(len(FEATURES)), decimal=6)
    np.testing.assert_array_almost_equal(result_df[FEATURES].std(), np.ones(len(FEATURES)), decimal=6)

def test_task_func_plot_histogram(sample_df, dict_mapping):
    result_df, ax = task_func(sample_df, dict_mapping, plot_histogram=True)
    assert isinstance(ax, plt.Axes)
    plt.close(ax.figure)  # Close the plot to avoid display issues in CI/CD environments

def test_task_func_no_plot(sample_df, dict_mapping):
    result_df, ax = task_func(sample_df, dict_mapping, plot_histogram=False)
    assert ax is None