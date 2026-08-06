import pytest
from src_0473 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_with_valid_input():
    # Test with a simple list of points and a valid number of clusters
    myList = [[1, 2], [2, 1], [3, 3], [8, 8], [8, 9]]
    n_clusters = 2
    ax = task_func(myList, n_clusters)
    
    # Check if the returned object is a matplotlib Axes
    assert isinstance(ax, plt.Axes)

def test_task_func_with_invalid_list():
    # Test with an empty list
    myList = []
    n_clusters = 3
    with pytest.raises(ValueError) as excinfo:
        task_func(myList, n_clusters)
    assert str(excinfo.value) == "Invalid inputs"

def test_task_func_with_invalid_n_clusters():
    # Test with non-positive number of clusters
    myList = [[1, 2], [2, 1], [3, 3], [8, 8], [8, 9]]
    n_clusters = -1
    with pytest.raises(ValueError) as excinfo:
        task_func(myList, n_clusters)
    assert str(excinfo.value) == "Invalid inputs"

def test_task_func_with_single_point():
    # Test with a single point in the list
    myList = [[1, 2]]
    n_clusters = 1
    ax = task_func(myList, n_clusters)
    
    # Check if the returned object is a matplotlib Axes
    assert isinstance(ax, plt.Axes)

def test_task_func_with_more_clusters_than_points():
    # Test with more clusters than points
    myList = [[1, 2], [2, 1]]
    n_clusters = 3
    ax = task_func(myList, n_clusters)
    
    # Check if the returned object is a matplotlib Axes
    assert isinstance(ax, plt.Axes)