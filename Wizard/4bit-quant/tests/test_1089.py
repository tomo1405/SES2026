python
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pytest

def task_func(data=None):
    if data is None:
        data = np.random.rand(100, 5)

    df = pd.DataFrame(data)
    df[df < 0.5] = 0

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)
    standardized_df = pd.DataFrame(scaled_data, columns=df.columns)

    return standardized_df

def test_task_func():
    # Test case 1: When data is None, it should return a standardized dataframe with random data
    standardized_df = task_func()
    assert isinstance(standardized_df, pd.DataFrame)
    assert standardized_df.shape == (100, 5)
    assert standardized_df.isnull().sum().sum() == 0

    # Test case 2: When data is provided, it should return a standardized dataframe with the provided data
    data = np.random.rand(100, 5)
    standardized_df = task_func(data)
    assert isinstance(standardized_df, pd.DataFrame)
    assert standardized_df.shape == (100, 5)
    assert standardized_df.isnull().sum().sum() == 0