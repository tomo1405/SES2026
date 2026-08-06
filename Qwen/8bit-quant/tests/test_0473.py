import pytest
from src_0473 import task_func
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

@pytest.fixture
def sample_data():
    return np.array([[1, 2], [1, 4], [1, 0],
                    [4, 2], [4, 4], [4, 0]])

def test_task_func_with_valid_inputs(sample_data):
    ax = task_func(sample_data, 2)
    assert isinstance(ax, plt.Axes)
    assert len(ax.collections) == 2  # scatter plot and cluster centers

def test_task_func_with_empty_list():
    with pytest.raises(ValueError, match="Invalid inputs"):
        task_func([], 2)

def test_task_func_with_non_positive_n_clusters():
    with pytest.raises(ValueError, match="Invalid inputs"):
        task_func(np.array([[1, 2], [1, 4]]), 0)

def test_task_func_with_single_point():
    ax = task_func(np.array([[1, 2]]), 1)
    assert isinstance(ax, plt.Axes)
    assert len(ax.collections) == 2  # scatter plot and cluster centers

def test_task_func_with_more_clusters_than_points():
    ax = task_func(np.array([[1, 2], [1, 4]]), 3)
    assert isinstance(ax, plt.Axes)
    assert len(ax.collections) == 2  # scatter plot and cluster centers