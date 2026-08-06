python
import pandas as pd
import pytest
from sklearn.cluster import KMeans

def task_func(x_list, y_list, n_clusters=2, random_state=0):
    df = pd.DataFrame({'x': x_list, 'y': y_list})
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state).fit(df)
    return kmeans.labels_, kmeans.cluster_centers_

def test_task_func():
    x_list = [1, 2, 3, 4, 5]
    y_list = [2, 3, 4, 5, 6]
    labels, centers = task_func(x_list, y_list)
    assert len(labels) == len(x_list)
    assert len(centers) == 2
    assert centers[0][0] == 2.5
    assert centers[1][0] == 4.5