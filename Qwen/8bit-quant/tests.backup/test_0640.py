import pytest
from src_0640 import task_func
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_default():
    df, ax = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (100, 5)
    assert all([f.startswith('Feature') for f in df.columns])
    assert all([s.startswith('Sample') for s in df.index])
    assert isinstance(ax, plt.Axes)

def test_task_func_custom_dimensions():
    df, ax = task_func(num_samples=50, num_features=3)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (50, 3)
    assert all([f.startswith('Feature') for f in df.columns])
    assert all([s.startswith('Sample') for s in df.index])
    assert isinstance(ax, plt.Axes)

def test_task_func_data_range():
    df, _ = task_func()
    assert df.values.min() >= 0
    assert df.values.max() <= 1

def test_task_func_corr_matrix():
    df, _ = task_func()
    corr_matrix = df.corr()
    assert isinstance(corr_matrix, pd.DataFrame)
    assert corr_matrix.shape == df.shape
    np.testing.assert_array_almost_equal(corr_matrix.values.T, corr_matrix.values)