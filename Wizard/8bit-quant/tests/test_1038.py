python
import pandas as pd
import pytest
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from src_1038 import task_func

def test_task_func():
    # Test case 1: valid input
    s1 = pd.Series([1, 2, 3, 4, 5])
    s2 = pd.Series([2, 4, 6, 8, 10])
    n_clusters = 2
    labels, ax = task_func(s1, s2, n_clusters)
    assert len(set(labels)) == n_clusters
    assert ax.get_xlabel() == s1.name
    assert ax.get_ylabel() == s2.name
    assert ax.get_title() == "K-Means Clustering"

    # Test case 2: invalid input (not pandas Series)
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 4, 6, 8, 10]
    with pytest.raises(ValueError):
        task_func(s1, s2)

    # Test case 3: invalid input (different lengths)
    s1 = pd.Series([1, 2, 3, 4, 5])
    s2 = pd.Series([2, 4, 6, 8])
    with pytest.raises(ValueError):
        task_func(s1, s2)