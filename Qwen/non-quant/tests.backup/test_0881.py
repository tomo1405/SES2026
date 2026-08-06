import pytest
from src_0881 import task_func
import pandas as pd
from sklearn.cluster import KMeans

def test_task_func_invalid_data():
    data = pd.DataFrame({
        'A': [1, 2, 'a'],
        'B': [4, 5, 6]
    })
    with pytest.raises(ValueError, match="DataFrame should only contain numeric values."):
        task_func(data)

def test_task_func_valid_data():
    data = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    labels, kmeans = task_func(data, n_clusters=2, seed=42)
    assert isinstance(labels, list)
    assert len(labels) == 3
    assert isinstance(kmeans, KMeans)
    assert kmeans.n_clusters == 2

def test_task_func_default_n_clusters():
    data = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    labels, kmeans = task_func(data)
    assert kmeans.n_clusters == 3

def test_task_func_random_state():
    data = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    labels1, kmeans1 = task_func(data, seed=42)
    labels2, kmeans2 = task_func(data, seed=42)
    assert labels1 == labels2