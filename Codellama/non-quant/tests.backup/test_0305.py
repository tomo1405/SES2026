import pytest
from src_0305 import task_func
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


def test_task_func_empty_df():
    df = pd.DataFrame()
    explained_variance_ratio, ax = task_func(df)
    assert explained_variance_ratio == 0
    assert ax is None


def test_task_func_non_empty_df():
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'Value': [1, 2, 3]})
    explained_variance_ratio, ax = task_func(df)
    assert isinstance(explained_variance_ratio, list)
    assert len(explained_variance_ratio) == 2
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Explained Variance Ratio of Principal Components'
    assert ax.get_xlabel() == 'Principal Component'
    assert ax.get_ylabel() == 'Explained Variance Ratio'