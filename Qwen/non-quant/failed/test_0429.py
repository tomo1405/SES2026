import pytest
from src_0429 import task_func
import pandas as pd
import numpy as np
import seaborn as sns

@pytest.fixture
def df1():
    return pd.DataFrame({
        'id': [1, 2, 3],
        'feature1': [10, 20, 30],
        'feature2': [40, 50, 60]
    })

@pytest.fixture
def df2():
    return pd.DataFrame({
        'id': [1, 2, 4],
        'feature3': [70, 80, 90]
    })

def test_task_func_merges_dataframes(df1, df2):
    merged_df, _ = task_func(df1, df2)
    expected_ids = [1, 2, 3, 4]
    assert list(merged_df['id']) == expected_ids

def test_task_func_scales_numeric_features(df1, df2):
    _, _ = task_func(df1, df2)
    # Assuming the scaling is correct if the mean is close to 0 and std is close to 1
    assert np.isclose(df1['feature1'].mean(), 0, atol=1e-6)
    assert np.isclose(df1['feature1'].std(), 1, atol=1e-6)

def test_task_func_returns_pair_plot(df1, df2):
    _, pair_plot = task_func(df1, df2)
    assert isinstance(pair_plot, sns.axisgrid.PairGrid)

def test_task_func_handles_empty_dataframes():
    empty_df1 = pd.DataFrame()
    empty_df2 = pd.DataFrame()
    merged_df, pair_plot = task_func(empty_df1, empty_df2)
    assert merged_df.empty
    assert pair_plot is None

def test_task_func_handles_non_numeric_columns(df1, df2):
    df1['non_numeric'] = ['a', 'b', 'c']
    merged_df, _ = task_func(df1, df2)
    assert 'non_numeric' not in merged_df.columns

def test_task_func_no_common_id(df1, df2):
    df2['id'] = [4, 5, 6]
    merged_df, _ = task_func(df1, df2)
    expected_ids = [1, 2, 3, 4, 5, 6]
    assert list(merged_df['id']) == expected_ids