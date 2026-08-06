import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from src_0978 import task_func
import pytest

def test_task_func_with_valid_input():
    array = np.array([[1, 2, 3], [4, 5, 6]])
    features = ["A", "B", "C"]
    seed = 42
    ax = task_func(array, features, seed)
    assert ax is not None
    assert isinstance(ax, plt.Axes)

def test_task_func_with_invalid_input():
    with pytest.raises(ValueError) as excinfo:
        array = np.array([])
        task_func(array)
    assert "Input array must be 2-dimensional and non-empty." in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        array = np.array([[1, 2, 3], [4, 5, 6]])
        features = ["A"]
        task_func(array, features)
    assert "Features list must match the number of columns in the array." in str(excinfo.value)