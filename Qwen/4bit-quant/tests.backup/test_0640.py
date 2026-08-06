import pytest
from src_0640 import task_func
import numpy as np
import pandas as pd
import seaborn as sns

def test_task_func_default():
    df, ax = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (100, 5)
    assert all(df.columns == ['Feature1', 'Feature2', 'Feature3', 'Feature4', 'Feature5'])
    assert all(df.index == [f'Sample{i}' for i in range(1, 101)])
    assert isinstance(ax, sns.axisgrid.FacetGrid)

def test_task_func_custom_dimensions():
    df, ax = task_func(num_samples=50, num_features=3)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (50, 3)
    assert all(df.columns == ['Feature1', 'Feature2', 'Feature3'])
    assert all(df.index == [f'Sample{i}' for i in range(1, 51)])
    assert isinstance(ax, sns.axisgrid.FacetGrid)

def test_task_func_random_data():
    df1, _ = task_func()
    df2, _ = task_func()
    assert not df1.equals(df2), "Random data should differ between runs"

def test_task_func_correlation_matrix():
    df, _ = task_func()
    corr_matrix = df.corr()
    assert isinstance(corr_matrix, pd.DataFrame)
    assert corr_matrix.shape == (5, 5)
    assert all(corr_matrix.columns == ['Feature1', 'Feature2', 'Feature3', 'Feature4', 'Feature5'])
    assert all(corr_matrix.index == ['Feature1', 'Feature2', 'Feature3', 'Feature4', 'Feature5'])

def test_task_func_heatmap_annotation():
    df, ax = task_func()
    corr_matrix = df.corr()
    for i in range(len(corr_matrix)):
        for j in range(len(corr_matrix)):
            annotation = ax.get_children()[i * len(corr_matrix) + j].get_text()
            assert float(annotation) == pytest.approx(corr_matrix.iat[i, j], abs=1e-2), "Heatmap annotations should match correlation matrix values"