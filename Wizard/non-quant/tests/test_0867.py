python
import numpy as np
import pytest
from sklearn.cluster import KMeans

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
    assert set(labels) == {0, 1}

def test_task_func_with_n_clusters():
    data = [('item1', 1, 2), ('item2', 3, 4), ('item3', 5, 6), ('item4', 7, 8)]
    labels = task_func(data, n_clusters=3)
    assert len(labels) == 4
    assert set(labels) == {0, 1, 2}

def test_task_func_with_random_state():
    data = [('item1', 1, 2), ('item2', 3, 4), ('item3', 5, 6), ('item4', 7, 8)]
    labels1 = task_func(data, random_state=0)
    labels2 = task_func(data, random_state=0)
    assert labels1 == labels2
    labels3 = task_func(data, random_state=1)
    assert labels1 != labels3

def test_task_func_with_empty_data():
    data = []
    labels = task_func(data)
    assert len(labels) == 0

def test_task_func_with_single_item():
    data = [('item1', 1, 2)]
    labels = task_func(data)
    assert len(labels) == 1
    assert labels[0] == 0

def test_task_func_with_single_cluster():
    data = [('item1', 1, 2), ('item2', 3, 4), ('item3', 5, 6)]
    labels = task_func(data)
    assert len(labels) == 3
    assert set(labels) == {0}

def test_task_func_with_two_clusters():
    data = [('item1', 1, 2), ('item2', 3, 4), ('item3', 5, 6), ('item4', 7, 8), ('item5', 9, 10)]
    labels = task_func(data)
    assert len(labels) == 5
    assert set(labels) == {0, 1}