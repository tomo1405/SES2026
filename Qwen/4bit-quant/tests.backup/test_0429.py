import pytest
from src_0429 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def df1():
    return pd.DataFrame({
        'id': [1, 2, 3],
        'feature1': [10, 20, 30],
        'feature2': [1.5, 2.5, 3.5]
    })

@pytest.fixture
def df2():
    return pd.DataFrame({
        'id': [2, 3, 4],
        'feature3': ['a', 'b', 'c']
    })

def test_task_func_merge(df1, df2):
    merged_df, _ = task_func(df1, df2)
    expected_ids = [1, 2, 3, 4]
    assert all(merged_df['id'] == expected_ids), "The merged DataFrame does not contain the correct ids"

def test_task_func_scaling(df1, df2):
    _, _ = task_func(df1, df2)
    # Assuming feature1 and feature2 are scaled, we can check the mean and std
    # Note: This is a simplified check and may need to be adjusted based on the actual scaling logic
    assert np.isclose(df1['feature1'].mean(), 0, atol=1e-6), "feature1 is not scaled correctly"
    assert np.isclose(df1['feature2'].std(), 1, atol=1e-6), "feature2 is not scaled correctly"

def test_task_func_pair_plot(df1, df2):
    _, pair_plot = task_func(df1, df2)
    assert pair_plot is not None, "Pair plot should not be None if there are numeric features"

def test_task_func_empty_df1(df2):
    empty_df1 = pd.DataFrame(columns=['id', 'feature1', 'feature2'])
    merged_df, _ = task_func(empty_df1, df2)
    assert merged_df.empty, "Merged DataFrame should be empty if df1 is empty"

def test_task_func_empty_df2(df1):
    empty_df2 = pd.DataFrame(columns=['id', 'feature3'])
    merged_df, _ = task_func(df1, empty_df2)
    assert merged_df.equals(df1), "Merged DataFrame should be equal to df1 if df2 is empty"

def test_task_func_no_numeric_features(df1, df2):
    df1_non_numeric = df1.copy()
    df1_non_numeric['feature1'] = df1_non_numeric['feature1'].astype(str)
    merged_df, _ = task_func(df1_non_numeric, df2)
    assert merged_df.equals(df1_non_numeric), "Merged DataFrame should be equal to df1 if there are no numeric features in df1"