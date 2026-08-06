import pandas as pd
from sklearn.cluster import KMeans
import pytest

def task_func(data, n_clusters=3, seed=None):
    if not data.apply(lambda s: pd.to_numeric(s, errors='coerce').notnull().all()).all():
        raise ValueError("DataFrame should only contain numeric values.")

    kmeans = KMeans(n_clusters=n_clusters, random_state=seed, n_init=10)
    kmeans.fit(data)

    return kmeans.labels_, kmeans

def test_task_func():
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    labels, kmeans = task_func(data)
    assert len(labels) == len(data)
    assert isinstance(kmeans, KMeans)

def test_task_func_with_invalid_data():
    data = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': ['d', 'e', 'f']})
    with pytest.raises(ValueError):
        task_func(data)