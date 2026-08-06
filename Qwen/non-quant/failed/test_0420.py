import pytest
from src_0420 import task_func
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

@pytest.fixture
def data():
    # Generate some random data for testing
    np.random.seed(0)
    X = np.random.rand(100, 5)  # 100 samples, 5 features
    Y = np.random.randint(0, 2, 100)  # Binary labels
    return X, Y

def test_task_func_output(data):
    X, Y = data
    model, ax = task_func(X, Y)
    
    # Check if the model is an instance of keras.models.Sequential
    assert isinstance(model, tf.keras.models.Sequential)
    
    # Check if the axes object is an instance of matplotlib.axes.Axes
    assert isinstance(ax, plt.Axes)
    
    # Check if the plot has the correct labels and title
    assert ax.get_xlabel() == 'Recall'
    assert ax.get_ylabel() == 'Precision'
    assert ax.get_title() == 'Precision-Recall Curve'
    
    # Check if the plot contains the Precision-Recall curve
    lines = ax.get_lines()
    assert len(lines) == 1
    assert lines[0].get_label() == 'Precision-Recall curve'

def test_task_func_model_training(data):
    X, Y = data
    model, _ = task_func(X, Y)
    
    # Check if the model has been trained with the correct number of epochs
    assert model.history.epoch[-1] == 199
    
    # Check if the model has the correct architecture
    layers = model.layers
    assert len(layers) == 1
    assert isinstance(layers[0], tf.keras.layers.Dense)
    assert layers[0].units == 1
    assert layers[0].input_dim == X.shape[1]
    assert layers[0].activation.__name__ == 'sigmoid'
    
    # Check if the model has been compiled with the correct loss and optimizer
    assert model.loss == 'binary_crossentropy'
    assert isinstance(model.optimizer, tf.keras.optimizers.SGD)
    assert model.optimizer.learning_rate.numpy() == 0.1