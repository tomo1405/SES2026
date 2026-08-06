import pytest
from src_0664 import task_func
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    x = [np.linspace(0, 10, 50), np.linspace(0, 20, 50)]
    y = [np.exp(-0.1 * x[0]) + np.random.normal(0, 0.1, len(x[0])),
         np.exp(-0.2 * x[1]) + np.random.normal(0, 0.1, len(x[1]))]
    labels = ['Curve 1', 'Curve 2']
    return x, y, labels

def test_task_func_with_valid_data(sample_data):
    x, y, labels = sample_data
    fig = task_func(x, y, labels)
    assert isinstance(fig, plt.Figure)

def test_task_func_with_empty_x(sample_data):
    x, y, labels = sample_data
    x = []
    with pytest.raises(ValueError, match="Empty data lists provided."):
        task_func(x, y, labels)

def test_task_func_with_empty_y(sample_data):
    x, y, labels = sample_data
    y = []
    with pytest.raises(ValueError, match="Empty data lists provided."):
        task_func(x, y, labels)

def test_task_func_with_empty_labels(sample_data):
    x, y, labels = sample_data
    labels = []
    with pytest.raises(ValueError, match="Empty data lists provided."):
        task_func(x, y, labels)

def test_task_func_with_mismatched_lengths(sample_data):
    x, y, labels = sample_data
    x.append(np.linspace(0, 30, 50))
    with pytest.raises(IndexError):
        task_func(x, y, labels)

def test_task_func_with_single_curve(sample_data):
    x, y, labels = sample_data
    x = [x[0]]
    y = [y[0]]
    labels = [labels[0]]
    fig = task_func(x, y, labels)
    assert isinstance(fig, plt.Figure)