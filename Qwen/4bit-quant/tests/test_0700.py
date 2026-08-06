import pytest
from src_0700 import task_func

def test_task_func_with_default_parameters():
    x_list = [1, 2, 3, 4, 5]
    y_list = [5, 4, 3, 2, 1]
    labels, centers = task_func(x_list, y_list)
    assert isinstance(labels, list)
    assert len(labels) == len(x_list)
    assert isinstance(centers, list)
    assert len(centers) == 2  # Default n_clusters is 2

def test_task_func_with_custom_n_clusters():
    x_list = [1, 2, 3, 4, 5]
    y_list = [5, 4, 3, 2, 1]
    labels, centers = task_func(x_list, y_list, n_clusters=3)
    assert isinstance(labels, list)
    assert len(labels) == len(x_list)
    assert isinstance(centers, list)
    assert len(centers) == 3

def test_task_func_with_empty_lists():
    x_list = []
    y_list = []
    labels, centers = task_func(x_list, y_list)
    assert labels == []
    assert centers == []

def test_task_func_with_single_point():
    x_list = [1]
    y_list = [1]
    labels, centers = task_func(x_list, y_list)
    assert labels == [0]
    assert len(centers) == 1

def test_task_func_with_identical_points():
    x_list = [1, 1, 1]
    y_list = [1, 1, 1]
    labels, centers = task_func(x_list, y_list)
    assert all(label == 0 for label in labels)
    assert len(centers) == 1

def test_task_func_with_negative_values():
    x_list = [-1, -2, -3, -4, -5]
    y_list = [-5, -4, -3, -2, -1]
    labels, centers = task_func(x_list, y_list)
    assert isinstance(labels, list)
    assert len(labels) == len(x_list)
    assert isinstance(centers, list)
    assert len(centers) == 2  # Default n_clusters is 2

def test_task_func_with_random_state():
    x_list = [1, 2, 3, 4, 5]
    y_list = [5, 4, 3, 2, 1]
    labels1, _ = task_func(x_list, y_list, random_state=0)
    labels2, _ = task_func(x_list, y_list, random_state=0)
    assert labels1 == labels2

def test_task_func_with_different_random_state():
    x_list = [1, 2, 3, 4, 5]
    y_list = [5, 4, 3, 2, 1]
    labels1, _ = task_func(x_list, y_list, random_state=0)
    labels2, _ = task_func(x_list, y_list, random_state=1)
    assert labels1 != labels2