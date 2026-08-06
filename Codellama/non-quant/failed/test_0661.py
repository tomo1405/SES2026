import pytest
from src_0661 import task_func
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler


def test_task_func():
    # Test case 1: x, y, and labels are all lists
    x = [[1, 2, 3], [4, 5, 6]]
    y = [[1, 2, 3], [4, 5, 6]]
    labels = ['label1', 'label2']
    fig = task_func(x, y, labels)
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    assert len(fig.axes[0].lines) == 2
    assert fig.axes[0].get_legend() is not None

    # Test case 2: x, y, and labels are all numpy arrays
    x = np.array([[1, 2, 3], [4, 5, 6]])
    y = np.array([[1, 2, 3], [4, 5, 6]])
    labels = np.array(['label1', 'label2'])
    fig = task_func(x, y, labels)
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    assert len(fig.axes[0].lines) == 2
    assert fig.axes[0].get_legend() is not None

    # Test case 3: x, y, and labels are all lists, but with different lengths
    x = [[1, 2, 3], [4, 5, 6, 7]]
    y = [[1, 2, 3], [4, 5, 6]]
    labels = ['label1', 'label2']
    with pytest.raises(ValueError):
        task_func(x, y, labels)

    # Test case 4: x, y, and labels are all numpy arrays, but with different lengths
    x = np.array([[1, 2, 3], [4, 5, 6, 7]])
    y = np.array([[1, 2, 3], [4, 5, 6]])
    labels = np.array(['label1', 'label2'])
    with pytest.raises(ValueError):
        task_func(x, y, labels)

    # Test case 5: x, y, and labels are all lists, but with different shapes
    x = [[1, 2, 3], [4, 5, 6]]
    y = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    labels = ['label1', 'label2']
    with pytest.raises(ValueError):
        task_func(x, y, labels)

    # Test case 6: x, y, and labels are all numpy arrays, but with different shapes
    x = np.array([[1, 2, 3], [4, 5, 6]])
    y = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    labels = np.array(['label1', 'label2'])
    with pytest.raises(ValueError):
        task_func(x, y, labels)