import pytest
from src_0700 import task_func
import pandas as pd
from sklearn.cluster import KMeans

@pytest.fixture
def x_list():
    return [1, 2, 3, 4, 5]

@pytest.fixture
def y_list():
    return [1, 2, 1, 2, 1]

def test_task_func(x_list, y_list):
    labels, centers = task_func(x_list, y_list)
    assert len(labels) == len(x_list)
    assert len(centers) == 2
    assert isinstance(labels, list)
    assert isinstance(centers, list)
    for center in centers:
        assert len(center) == 2

def test_task_func_with_n_clusters(x_list, y_list):
    labels, centers = task_func(x_list, y_list, n_clusters=3)
    assert len(centers) == 3

def test_task_func_with_random_state(x_list, y_list):
    labels_1, _ = task_func(x_list, y_list, random_state=0)
    labels_2, _ = task_func(x_list, y_list, random_state=0)
    assert labels_1 == labels_2

def test_task_func_with_invalid_input(x_list, y_list):
    with pytest.raises(ValueError):
        task_func(x_list, y_list, n_clusters=0)
    with pytest.raises(ValueError):
        task_func(x_list, y_list, n_clusters=-1)
    with pytest.raises(ValueError):
        task_func(x_list, y_list, n_clusters='invalid')
    with pytest.raises(ValueError):
        task_func(x_list, y_list, random_state='invalid')