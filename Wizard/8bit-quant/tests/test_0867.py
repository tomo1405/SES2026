python
import numpy as np
from sklearn.cluster import KMeans
import pytest

def task_func(data, n_clusters=2, random_state=0):
    items, x_values, y_values = zip(*data)
    coordinates = np.array(list(zip(x_values, y_values)))

    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state).fit(coordinates)
    labels = kmeans.labels_

    return labels

def test_task_func():
    data = [('item1', 1, 2), ('item2', 3, 4), ('item3', 5, 6), ('item4', 7, 8)]
    labels = task_func(data)
    assert len(labels) == 4
    assert labels == [0, 0, 1, 1]