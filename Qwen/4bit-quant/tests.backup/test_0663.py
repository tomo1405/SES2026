import pytest
from src_0663 import task_func
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def test_task_func_with_valid_data():
    x = [[1, 2, 3], [4, 5, 6]]
    y = [[7, 8, 9], [10, 11, 12]]
    labels = ['A', 'B']
    
    fig = task_func(x, y, labels)
    
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    assert len(fig.axes[0].lines) == 2  # One line per label

def test_task_func_with_single_point():
    x = [[1], [4]]
    y = [[7], [10]]
    labels = ['A']
    
    fig = task_func(x, y, labels)
    
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    assert len(fig.axes[0].lines) == 1

def test_task_func_with_empty_data():
    x = []
    y = []
    labels = []
    
    fig = task_func(x, y, labels)
    
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    assert len(fig.axes[0].lines) == 0

def test_task_func_with_single_label():
    x = [[1, 2], [3, 4]]
    y = [[5, 6], [7, 8]]
    labels = ['A']
    
    fig = task_func(x, y, labels)
    
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    assert len(fig.axes[0].lines) == 1

def test_task_func_with_multiple_labels():
    x = [[1, 2], [3, 4], [5, 6]]
    y = [[7, 8], [9, 10], [11, 12]]
    labels = ['A', 'B', 'C']
    
    fig = task_func(x, y, labels)
    
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    assert len(fig.axes[0].lines) == 3

def test_task_func_with_pca_decomposition():
    x = [[1, 2], [3, 4]]
    y = [[5, 6], [7, 8]]
    labels = ['A', 'B']
    
    fig = task_func(x, y, labels)
    
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    
    # Check if PCA is applied correctly
    pca = PCA(n_components=2)
    xy = np.vstack((x[0], y[0])).T
    xy_transformed = pca.fit_transform(xy)
    assert xy_transformed.shape == (2, 2)