import pandas as pd
import pytest
from sklearn.cluster import KMeans
from src_0881 import task_func

@pytest.fixture
def data():
    return pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8],
        'C': [9, 10, 11, 12]
    })

def test_task_func_with_numeric_data(data):
    labels, kmeans = task_func(data)
    assert isinstance(labels, list)
    assert isinstance(kmeans, KMeans)

def test_task_func_with_non_numeric_data(data):
    data['D'] = ['a', 'b', 'c', 'd']
    with pytest.raises(ValueError):
        task_func(data)

def test_task_func_with_invalid_n_clusters(data):
    with pytest.raises(ValueError):
        task_func(data, n_clusters=0)
    with pytest.raises(ValueError):
        task_func(data, n_clusters=-1)

def test_task_func_with_invalid_seed(data):
    with pytest.raises(ValueError):
        task_func(data, seed='abc')