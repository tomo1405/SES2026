import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest
from src_0093 import task_func


def test_task_func_input_data_not_dataframe():
    data = [1, 2, 3]
    n_clusters = 3
    with pytest.raises(ValueError):
        task_func(data, n_clusters)

def test_task_func_input_n_clusters_not_int():
    data = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
    n_clusters = '3'
    with pytest.raises(ValueError):
        task_func(data, n_clusters)

def test_task_func_input_n_clusters_less_than_1():
    data = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
    n_clusters = 0
    with pytest.raises(ValueError):
        task_func(data, n_clusters)

def test_task_func_output_labels_not_array():
    data = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
    n_clusters = 3
    labels, ax = task_func(data, n_clusters)
    assert isinstance(labels, np.ndarray)

def test_task_func_output_ax_not_axes():
    data = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
    n_clusters = 3
    labels, ax = task_func(data, n_clusters)
    assert isinstance(ax, plt.Axes)

def test_task_func_output_ax_has_correct_labels():
    data = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
    n_clusters = 3
    labels, ax = task_func(data, n_clusters)
    assert ax.get_legend_handles_labels()[1] == ['Data points', 'Centroids']

def test_task_func_output_ax_has_correct_title():
    data = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
    n_clusters = 3
    labels, ax = task_func(data, n_clusters)
    assert ax.get_title() == 'K-Means Clustering'

def test_task_func_output_ax_has_correct_xlabel():
    data = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
    n_clusters = 3
    labels, ax = task_func(data, n_clusters)
    assert ax.get_xlabel() == 'Feature 1'

def test_task_func_output_ax_has_correct_ylabel():
    data = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
    n_clusters = 3
    labels, ax = task_func(data, n_clusters)
    assert ax.get_ylabel() == 'Feature 2'