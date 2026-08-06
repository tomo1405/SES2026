import pytest
from src_0094 import task_func
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def test_task_func():
    data = np.random.rand(10, 3)
    n_components = 2
    expected_columns = ['PC1', 'PC2']
    expected_ax = plt.subplots()

    result, ax = task_func(data, n_components)

    assert isinstance(result, pd.DataFrame)
    assert result.shape == (10, 2)
    assert result.columns.tolist() == expected_columns
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'PC1'
    assert ax.get_ylabel() == 'PC2'
    assert ax.get_title() == 'PCA'