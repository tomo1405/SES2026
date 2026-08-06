import pytest
from src_0664 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_empty_data():
    with pytest.raises(ValueError, match="Empty data lists provided."):
        task_func([], [], [])

def test_task_func_single_dataset():
    x = [[1, 2, 3]]
    y = [[2, 5, 9]]
    labels = ["Dataset 1"]
    fig = task_func(x, y, labels)
    assert isinstance(fig, plt.Figure)

def test_task_func_multiple_datasets():
    x = [[1, 2, 3], [4, 5, 6]]
    y = [[2, 5, 9], [1, 3, 7]]
    labels = ["Dataset 1", "Dataset 2"]
    fig = task_func(x, y, labels)
    assert isinstance(fig, plt.Figure)

def test_task_func_with_zero_values():
    x = [[0, 0, 0]]
    y = [[0, 0, 0]]
    labels = ["Zero Dataset"]
    fig = task_func(x, y, labels)
    assert isinstance(fig, plt.Figure)

def test_task_func_with_negative_values():
    x = [[-1, -2, -3]]
    y = [[2, 5, 9]]
    labels = ["Negative X"]
    fig = task_func(x, y, labels)
    assert isinstance(fig, plt.Figure)

def test_task_func_with_non_exponential_data():
    x = [[1, 2, 3]]
    y = [[1, 2, 3]]  # Linear data
    labels = ["Linear Data"]
    fig = task_func(x, y, labels)
    assert isinstance(fig, plt.Figure)