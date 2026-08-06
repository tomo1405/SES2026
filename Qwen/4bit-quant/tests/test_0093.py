import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest
from src_0093 import task_func


def test_task_func_input_data_type():
    with pytest.raises(ValueError, match="Input 'data' must be a pandas DataFrame."):
        task_func([1, 2, 3])

def test_task_func_n_clusters_type():
    with pytest.raises(ValueError, match="'n_clusters' must be an integer greater than 1."):
        task_func(pd.DataFrame([[1, 2], [3, 4]]), n_clusters=1)

def test_task_func_n_clusters_value():
    with pytest.raises(ValueError, match="'n_clusters' must be an integer greater than 1."):
        task_func(pd.DataFrame([[1, 2], [3, 4]]), n_clusters=0)

def test_task_func_return_values():
    data = pd.DataFrame({
        'Feature 1': [1, 2, 3, 4, 5],
        'Feature 2': [5, 4, 3, 2, 1]
    })
    labels, ax = task_func(data, n_clusters=3)
    assert isinstance(labels, np.ndarray)
    assert len(labels) == 5
    assert isinstance(ax, plt.Axes)
    assert isinstance(ax.collections[0], PathCollection)
    assert isinstance(ax.collections[1], PathCollection)