import pytest
from src_0881 import task_func
import pandas as pd
from sklearn.cluster import KMeans

def test_task_func_valid_input():
    data = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    labels, kmeans = task_func(data)
    assert labels.shape == (3,)
    assert kmeans.n_clusters == 3
    assert kmeans.n_init == 10

def test_task_func_invalid_input():
    data = pd.DataFrame({'a': [1, 2, 3], 'b': ['a', 'b', 'c']})
    with pytest.raises(ValueError):
        task_func(data)