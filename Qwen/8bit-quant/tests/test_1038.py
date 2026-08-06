import pytest
from src_1038 import task_func
import pandas as pd
import numpy as np

def test_task_func_input_types():
    s1 = pd.Series([1, 2, 3])
    s2 = pd.Series([4, 5, 6])
    labels, ax = task_func(s1, s2)
    assert isinstance(labels, np.ndarray)
    assert isinstance(ax, plt.Axes)

def test_task_func_input_length_mismatch():
    s1 = pd.Series([1, 2, 3])
    s2 = pd.Series([4, 5])
    with pytest.raises(ValueError, match="s1 and s2 must have the same length"):
        task_func(s1, s2)

def test_task_func_non_series_input():
    s1 = [1, 2, 3]
    s2 = pd.Series([4, 5, 6])
    with pytest.raises(ValueError, match="s1 and s2 must be pandas Series"):
        task_func(s1, s2)

def test_task_func_n_clusters():
    s1 = pd.Series([1, 2, 3, 4, 5])
    s2 = pd.Series([6, 7, 8, 9, 10])
    labels, ax = task_func(s1, s2, n_clusters=2)
    assert len(np.unique(labels)) == 2

def test_task_func_default_n_clusters():
    s1 = pd.Series([1, 2, 3])
    s2 = pd.Series([4, 5, 6])
    labels, ax = task_func(s1, s2)
    assert len(np.unique(labels)) == 3

def test_task_func_plot_labels():
    s1 = pd.Series([1, 2, 3])
    s2 = pd.Series([4, 5, 6])
    labels, ax = task_func(s1, s2)
    scatter = ax.collections[0]
    assert len(scatter.get_offsets()) == len(s1)
    assert len(scatter.get_array()) == len(s1)