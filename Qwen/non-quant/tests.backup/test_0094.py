import pytest
from src_0094 import task_func
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def test_task_func_input_validation():
    with pytest.raises(ValueError):
        task_func(np.array([[1, 2], [3, 4]]), n_components=-1)
    with pytest.raises(ValueError):
        task_func(np.array([[1, 2], [3, 4]]), n_components=0)
    with pytest.raises(ValueError):
        task_func(np.array([[1, 2], [3, 4]]), n_components=1.5)
    with pytest.raises(ValueError):
        task_func(np.array([[1, 2], [3, 4]]), n_components="string")

def test_task_func_output_shape():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    df, ax = task_func(data, n_components=2)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 2)
    assert len(ax.collections) == 1  # Check if scatter plot is created

def test_task_func_column_names():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    df, _ = task_func(data, n_components=2)
    assert list(df.columns) == ['PC1', 'PC2']

def test_task_func_pca_transformation():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    expected_transformed_data = PCA(n_components=2).fit_transform(data)
    df, _ = task_func(data, n_components=2)
    assert np.allclose(df.values, expected_transformed_data)

def test_task_func_random_state():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    df1, _ = task_func(data, n_components=2)
    df2, _ = task_func(data, n_components=2)
    assert df1.equals(df2)

def test_task_func_plot():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    _, ax = task_func(data, n_components=2)
    assert isinstance(ax, plt.Axes)
    assert len(ax.collections) == 1  # Check if scatter plot is created