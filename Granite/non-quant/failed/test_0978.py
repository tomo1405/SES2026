import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pytest

from src_0978 import task_func

def test_task_func():
    array = np.array([[1, 2, 3], [4, 5, 6]])
    features = ['A', 'B', 'C']
    seed = 42

    with pytest.raises(ValueError):
        task_func(np.array([]))  # Test for empty array
    with pytest.raises(ValueError):
        task_func(np.array([[]]))  # Test for 1D array
    with pytest.raises(ValueError):
        task_func(np.array([[1], [2], [3]]))  # Test for 3D array
    with pytest.raises(ValueError):
        task_func(array, features=features[:-1])  # Test for mismatched features and columns

    ax = task_func(array, features=features, seed=seed)

    assert isinstance(ax, plt.Axes)  # Test for correct return type
    assert ax.get_xlabel() == 'A'  # Test for correct x-label
    assert ax.get_ylabel() == 'B'  # Test for correct y-label
    assert ax.get_title() == 'Heatmap'  # Test for correct title