import matplotlib.pyplot as plt
import numpy as np
from keras.models import Model
from src_0418 import task_func


def test_task_func_output():
    # Sample data
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    Y = np.array([0, 1, 1, 0])

    model, ax = task_func(X, Y)

    # Check if the model is an instance of keras.models.Model
    assert isinstance(model, Model)

    # Check if the ax is an instance of matplotlib.axes.Axes
    assert isinstance(ax, plt.Axes)

def test_task_func_model_structure():
    # Sample data
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    Y = np.array([0, 1, 1, 0])

    model, _ = task_func(X, Y)

    # Check if the model has the correct number of layers
    assert len(model.layers) == 1

    # Check if the layer is an instance of Dense
    assert isinstance(model.layers[0], Dense)

    # Check if the layer has the correct input_dim and units
    assert model.layers[0].input_dim == 2
    assert model.layers[0].units == 1

    # Check if the layer has the correct activation function
    assert model.layers[0].activation.__name__ == 'sigmoid'

def test_task_func_model_training():
    # Sample data
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    Y = np.array([0, 1, 1, 0])

    model, _ = task_func(X, Y)

    # Check if the model has been trained
    assert hasattr(model, 'history')

    # Check if the history contains 'loss' and 'val_loss'
    assert 'loss' in model.history
    assert 'val_loss' in model.history

    # Check if the lengths of 'loss' and 'val_loss' are equal to the number of epochs
    assert len(model.history['loss']) == 200
    assert len(model.history['val_loss']) == 200