import pytest
from src_1038 import task_func
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def test_task_func():
    s1 = pd.Series([1, 2, 3, 4, 5])
    s2 = pd.Series([2, 4, 6, 8, 10])
    n_clusters = 3

    labels, ax = task_func(s1, s2, n_clusters)

    assert isinstance(labels, pd.Series)
    assert isinstance(ax, plt.Axes)
    assert len(labels) == len(s1)
    assert len(labels) == len(s2)
    assert len(labels) == n_clusters

def test_task_func_invalid_input():
    s1 = pd.Series([1, 2, 3, 4, 5])
    s2 = pd.Series([2, 4, 6, 8, 10])
    n_clusters = 3

    with pytest.raises(ValueError):
        task_func(s1, s2, n_clusters=0)

    with pytest.raises(ValueError):
        task_func(s1, s2, n_clusters=100)

    with pytest.raises(ValueError):
        task_func(s1, s2, n_clusters="3")

    with pytest.raises(ValueError):
        task_func(s1, s2, n_clusters=None)

def test_task_func_invalid_series():
    s1 = pd.Series([1, 2, 3, 4, 5])
    s2 = pd.Series([2, 4, 6, 8, 10])
    n_clusters = 3

    with pytest.raises(ValueError):
        task_func(s1, s2, n_clusters=n_clusters, random_state=42)

    with pytest.raises(ValueError):
        task_func(s1, s2, n_clusters=n_clusters, n_init=10)

    with pytest.raises(ValueError):
        task_func(s1, s2, n_clusters=n_clusters, random_state=42, n_init=10)