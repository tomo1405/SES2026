import numpy as np
import pandas as pd
import pytest
import seaborn as sns
from src_0158 import task_func


def test_task_func():
    # Test 1: Input data is not a 2D numpy array
    data = np.array([[1, 2, 3], [4, 5, 6]])
    with pytest.raises(ValueError):
        task_func(data)

    # Test 2: Input data is a 2D numpy array
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    df, ax = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, sns.heatmap)
    assert 'Average' in df.columns
    assert df['Average'].dtype == np.float64

    # Test 3: Input data is a 2D numpy array with a different dtype
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.int64)
    df, ax = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, sns.heatmap)
    assert 'Average' in df.columns
    assert df['Average'].dtype == np.float64

    # Test 4: Input data is a 2D numpy array with a different shape
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    df, ax = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, sns.heatmap)
    assert 'Average' in df.columns
    assert df['Average'].dtype == np.float64

    # Test 5: Input data is a 2D numpy array with a different shape and dtype
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], dtype=np.int64)
    df, ax = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, sns.heatmap)
    assert 'Average' in df.columns
    assert df['Average'].dtype == np.float64