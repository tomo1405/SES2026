import matplotlib.pyplot as plt
import pytest
from src_0664 import task_func


def test_task_func_empty_data():
    with pytest.raises(ValueError, match="Empty data lists provided."):
        task_func([], [], [])

def test_task_func_single_dataset():
    x = [[1, 2, 3]]
    y = [[1, 0.5, 0.25]]
    labels = ["Dataset 1"]
    fig = task_func(x, y, labels)
    assert isinstance(fig, plt.Figure)

def test_task_func_multiple_datasets():
    x = [[1, 2, 3], [4, 5, 6]]
    y = [[1, 0.5, 0.25], [0.5, 0.25, 0.125]]
    labels = ["Dataset 1", "Dataset 2"]
    fig = task_func(x, y, labels)
    assert isinstance(fig, plt.Figure)

def test_task_func_non_exponential_data():
    x = [[1, 2, 3]]
    y = [[1, 2, 3]]  # Linear data, not exponential
    labels = ["Dataset 1"]
    fig = task_func(x, y, labels)
    assert isinstance(fig, plt.Figure)

def test_task_func_invalid_input_types():
    with pytest.raises(TypeError):
        task_func([1, 2, 3], [1, 2, 3], "label")  # labels should be a list
    with pytest.raises(TypeError):
        task_func(1, [1, 2, 3], ["label"])  # x should be a list of lists
    with pytest.raises(TypeError):
        task_func([1, 2, 3], 1, ["label"])  # y should be a list of lists

def test_task_func_different_lengths():
    with pytest.raises(ValueError):
        task_func([[1, 2, 3]], [[1, 2]], ["Dataset 1"])  # x and y have different lengths
    with pytest.raises(ValueError):
        task_func([[1, 2, 3]], [[1, 2, 3]], ["Dataset 1", "Dataset 2"])  # x and labels have different lengths