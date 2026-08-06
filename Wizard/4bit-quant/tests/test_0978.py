python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pytest

from src_0978 import task_func

def test_task_func():
    # Test case 1: Valid input array, no features, no seed
    array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    ax = task_func(array)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Heatmap of shuffled array"
    assert ax.get_xlabel() == "Column"
    assert ax.get_ylabel() == "Row"
    assert ax.get_xticks() == [1, 2, 3]
    assert ax.get_yticks() == [1, 2, 3]
    assert ax.collections[0].get_array().shape == (3, 3)

    # Test case 2: Valid input array, features, no seed
    array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    features = ["A", "B", "C"]
    ax = task_func(array, features)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Heatmap of shuffled array"
    assert ax.get_xlabel() == "Feature"
    assert ax.get_ylabel() == "Row"
    assert ax.get_xticks() == [1, 2, 3]
    assert ax.get_yticks() == [1, 2, 3]
    assert ax.collections[0].get_array().shape == (3, 3)

    # Test case 3: Valid input array, no features, seed
    array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    seed = 42
    ax = task_func(array, seed=seed)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Heatmap of shuffled array"
    assert ax.get_xlabel() == "Column"
    assert ax.get_ylabel() == "Row"
    assert ax.get_xticks() == [1, 2, 3]
    assert ax.get_yticks() == [1, 2, 3]
    assert ax.collections[0].get_array().shape == (3, 3)

    # Test case 4: Invalid input array (empty), no features, no seed
    array = np.array([])
    with pytest.raises(ValueError):
        task_func(array)

    # Test case 5: Invalid input array (not 2-dimensional), no features, no seed
    array = np.array([1, 2, 3])
    with pytest.raises(ValueError):
        task_func(array)

    # Test case 6: Invalid features list (wrong length), no seed
    array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    features = ["A", "B"]
    with pytest.raises(ValueError):
        task_func(array, features)

    # Test case 7: Invalid seed (not an integer), no features
    array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    seed = "42"
    with pytest.raises(ValueError):
        task_func(array, seed=seed)