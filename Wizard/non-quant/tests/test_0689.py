python
import pandas as pd
import pytest
from sklearn.preprocessing import StandardScaler

def task_func(df):
    # Standardize data
    scaler = StandardScaler()
    df_standardized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    return df_standardized

def test_task_func():
    # Test case 1
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    expected_df = pd.DataFrame({'A': [-1.22474487, 0., 1.22474487], 'B': [-1.22474487, 0., 1.22474487]})
    assert task_func(df).equals(expected_df)

    # Test case 2
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    expected_df = pd.DataFrame({'A': [-1.22474487, 0., 1.22474487], 'B': [-1.22474487, 0., 1.22474487], 'C': [-1.22474487, 0., 1.22474487]})
    assert task_func(df).equals(expected_df)

    # Test case 3
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12]})
    expected_df = pd.DataFrame({'A': [-1.22474487, 0., 1.22474487], 'B': [-1.22474487, 0., 1.22474487], 'C': [-1.22474487, 0., 1.22474487], 'D': [-1.22474487, 0., 1.22474487]})
    assert task_func(df).equals(expected_df)