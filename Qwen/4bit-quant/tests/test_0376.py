import pytest
from src_0376 import task_func
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    return np.array([[1, 2], [3, 4], [5, 6]])

def test_task_func_returns_axis_object(sample_data):
    ax = task_func(sample_data)
    assert isinstance(ax, plt.Axes)

def test_task_func_plot(sample_data, monkeypatch):
    def mock_scatter(x, y):
        assert len(x) == 3
        assert len(y) == 3
    
    monkeypatch.setattr(plt, 'scatter', mock_scatter)
    task_func(sample_data)

def test_task_func_labels_and_title(sample_data, monkeypatch):
    def mock_xlabel(label):
        assert label == 'First Principal Component'
    
    def mock_ylabel(label):
        assert label == 'Second Principal Component'
    
    def mock_title(title):
        assert title == 'PCA Result'
    
    monkeypatch.setattr(plt, 'xlabel', mock_xlabel)
    monkeypatch.setattr(plt, 'ylabel', mock_ylabel)
    monkeypatch.setattr(plt, 'title', mock_title)
    task_func(sample_data)