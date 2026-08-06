import pytest
from src_0094 import task_func
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def test_task_func():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    n_components = 2
    expected_columns = ['PC1', 'PC2']
    expected_data = np.array([[1, 2], [3, 4], [5, 6]])

    result, ax = task_func(data, n_components)

    assert isinstance(result, pd.DataFrame)
    assert result.columns.tolist() == expected_columns
    assert np.allclose(result.values, expected_data)

    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'PC1'
    assert ax.get_ylabel() == 'PC2'
    assert ax.get_title() == 'PCA Plot'

def test_task_func_invalid_n_components():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    n_components = -1

    with pytest.raises(ValueError):
        task_func(data, n_components)

def test_task_func_invalid_data():
    data = 'invalid data'
    n_components = 2

    with pytest.raises(ValueError):
        task_func(data, n_components)