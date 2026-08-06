import matplotlib.pyplot as plt
import numpy as np
import pytest
import tensorflow as tf
from src_0420 import task_func


@pytest.fixture
def sample_data():
    # Create a simple binary classification dataset
    np.random.seed(42)
    X = np.random.rand(100, 5)
    Y = (X.sum(axis=1) > 2.5).astype(int)
    return X, Y

def test_task_func(sample_data):
    X, Y = sample_data
    model, ax = task_func(X, Y)
    
    # Check if the model is an instance of Sequential
    assert isinstance(model, tf.keras.models.Sequential)
    
    # Check if the axes object is an instance of matplotlib.axes.Axes
    assert isinstance(ax, plt.Axes)
    
    # Check if the model has been trained
    assert len(model.history.history) == 200
    
    # Check if the precision-recall curve plot has been created
    lines = ax.get_lines()
    assert len(lines) == 1
    assert lines[0].get_label() == 'Precision-Recall curve'
    
    # Check if the plot has the correct labels and title
    assert ax.get_xlabel() == 'Recall'
    assert ax.get_ylabel() == 'Precision'
    assert ax.get_title() == 'Precision-Recall Curve'

def test_task_func_with_zero_samples():
    X = np.array([])
    Y = np.array([])
    with pytest.raises(ValueError):
        task_func(X, Y)

def test_task_func_with_one_class():
    X = np.random.rand(100, 5)
    Y = np.zeros(100)
    model, ax = task_func(X, Y)
    
    # Check if the model is an instance of Sequential
    assert isinstance(model, tf.keras.models.Sequential)
    
    # Check if the axes object is an instance of matplotlib.axes.Axes
    assert isinstance(ax, plt.Axes)
    
    # Check if the model has been trained
    assert len(model.history.history) == 200
    
    # Check if the precision-recall curve plot has been created
    lines = ax.get_lines()
    assert len(lines) == 1
    assert lines[0].get_label() == 'Precision-Recall curve'
    
    # Check if the plot has the correct labels and title
    assert ax.get_xlabel() == 'Recall'
    assert ax.get_ylabel() == 'Precision'
    assert ax.get_title() == 'Precision-Recall Curve'