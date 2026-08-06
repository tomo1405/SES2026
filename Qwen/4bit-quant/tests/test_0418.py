import matplotlib.pyplot as plt
import numpy as np
import pytest
from src_0418 import task_func


@pytest.fixture
def sample_data():
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    Y = np.array([0, 1, 1, 0])
    return X, Y

def test_task_func(sample_data):
    X, Y = sample_data
    model, ax = task_func(X, Y)
    
    # Check if the model is an instance of Sequential
    assert isinstance(model, Sequential)
    
    # Check if the plot is an AxesSubplot instance
    assert isinstance(ax, plt.Axes)
    
    # Check if the model has been trained (by checking the number of layers)
    assert len(model.layers) == 1
    
    # Check if the model has been compiled (by checking the optimizer)
    assert model.optimizer.lr.numpy() == 0.1

# This test checks if the function raises an error when given invalid input shapes
def test_task_func_invalid_input(sample_data):
    X, Y = sample_data
    X_invalid = X.reshape(-1, 1)  # Invalid shape by reducing dimensions
    with pytest.raises(ValueError):
        task_func(X_invalid, Y)

# This test checks if the function raises an error when given mismatched input and output shapes
def test_task_func_mismatched_shapes(sample_data):
    X, Y = sample_data
    Y_invalid = Y.reshape(-1, 2)  # Mismatched shape by increasing dimensions
    with pytest.raises(ValueError):
        task_func(X, Y_invalid)