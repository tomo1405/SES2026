import pytest
from src_0093 import task_func
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from matplotlib.figure import Figure
from matplotlib.axes import Axes

def test_task_func_invalid_data_type():
    with pytest.raises(ValueError, match="Input 'data' must be a pandas DataFrame."):
        task_func([1, 2, 3])

def test_task_func_invalid_n_clusters():
    data = pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6]})
    with pytest.raises(ValueError, match="'n_clusters' must be an integer greater than 1."):
        task_func(data, n_clusters=1)

def test_task_func_valid_input():
    data = pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6]})
    labels, ax = task_func(data, n_clusters=2)
    
    assert isinstance(labels, np.ndarray)
    assert len(labels) == len(data)
    assert isinstance(ax, Axes)
    assert isinstance(ax.get_figure(), Figure)

def test_task_func_kmeans_fit_predict():
    data = pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6]})
    labels, _ = task_func(data, n_clusters=2)
    
    kmeans = KMeans(n_clusters=2)
    expected_labels = kmeans.fit_predict(data)
    
    assert np.array_equal(labels, expected_labels)

def test_task_func_plot_content():
    data = pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6]})
    _, ax = task_func(data, n_clusters=2)
    
    lines = ax.get_lines()
    collections = ax.collections
    
    assert len(lines) == 1  # Centroids line
    assert isinstance(lines[0], plt.Line2D)
    assert len(collections) == 1  # Data points scatter
    assert isinstance(collections[0], PathCollection)