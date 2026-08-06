import pytest
from src_0305 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_df():
    data = {
        'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'Value': [[1, 2], [3, 4], [5, 6]]
    }
    return pd.DataFrame(data)

def test_task_func_with_empty_df():
    empty_df = pd.DataFrame()
    explained_variance_ratio, ax = task_func(empty_df)
    assert explained_variance_ratio == 0
    assert ax is None

def test_task_func_with_sample_df(sample_df):
    explained_variance_ratio, ax = task_func(sample_df)
    assert isinstance(explained_variance_ratio, np.ndarray)
    assert len(explained_variance_ratio) > 0
    assert isinstance(ax, plt.Axes)

def test_task_func_data_preparation(sample_df):
    explained_variance_ratio, ax = task_func(sample_df)
    assert 'Date' in sample_df.columns
    assert all(isinstance(date, pd.Timestamp) for date in sample_df['Date'])

def test_task_func_pca_application(sample_df):
    explained_variance_ratio, ax = task_func(sample_df)
    assert isinstance(explained_variance_ratio, np.ndarray)
    assert explained_variance_ratio.sum() <= 1.0

def test_task_func_plot(sample_df):
    explained_variance_ratio, ax = task_func(sample_df)
    assert ax.get_title() == 'Explained Variance Ratio of Principal Components'
    assert ax.get_xlabel() == 'Principal Component'
    assert ax.get_ylabel() == 'Explained Variance Ratio'