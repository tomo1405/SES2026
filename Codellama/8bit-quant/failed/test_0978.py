import pytest
from src_0978 import task_func
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def test_task_func():
    # Test case 1: input array is 2-dimensional and non-empty
    array = np.array([[1, 2, 3], [4, 5, 6]])
    features = ["feature1", "feature2", "feature3"]
    ax = task_func(array, features)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Heatmap"
    assert ax.get_xlabel() == "feature1"
    assert ax.get_ylabel() == "feature2"
    assert ax.get_zlabel() == "feature3"

    # Test case 2: input array is 2-dimensional and non-empty, but features is None
    array = np.array([[1, 2, 3], [4, 5, 6]])
    ax = task_func(array)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Heatmap"
    assert ax.get_xlabel() == "1"
    assert ax.get_ylabel() == "2"
    assert ax.get_zlabel() == "3"

    # Test case 3: input array is not 2-dimensional
    array = np.array([1, 2, 3])
    with pytest.raises(ValueError):
        task_func(array)

    # Test case 4: input array is empty
    array = np.array([])
    with pytest.raises(ValueError):
        task_func(array)

    # Test case 5: features list does not match the number of columns in the array
    array = np.array([[1, 2, 3], [4, 5, 6]])
    features = ["feature1", "feature2"]
    with pytest.raises(ValueError):
        task_func(array, features)