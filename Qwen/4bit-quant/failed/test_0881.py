import pytest
from src_0881 import task_func
import pandas as pd
import numpy as np

def test_task_func_valid_data():
    data = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    labels, kmeans_model = task_func(data, n_clusters=2, seed=42)
    assert isinstance(labels, np.ndarray)
    assert len(labels) == 3
    assert isinstance(kmeans_model, KMeans)

def test_task_func_invalid_data():
    data = pd.DataFrame({
        'A': [1, 2, 'a'],
        'B': [4, 5, 6]
    })
    with pytest.raises(ValueError, match="DataFrame should only contain numeric values."):
        task_func(data, n_clusters=2, seed=42)

def test_task_func_single_cluster():
    data = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    labels, kmeans_model = task_func(data, n_clusters=1, seed=42)
    assert isinstance(labels, np.ndarray)
    assert len(labels) == 3
    assert np.all(labels == 0)
    assert isinstance(kmeans_model, KMeans)

def test_task_func_no_clusters():
    data = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    with pytest.raises(ValueError):
        task_func(data, n_clusters=0, seed=42)

def test_task_func_large_clusters():
    data = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    labels, kmeans_model = task_func(data, n_clusters=4, seed=42)
    assert isinstance(labels, np.ndarray)
    assert len(labels) == 3
    assert isinstance(kmeans_model, KMeans)