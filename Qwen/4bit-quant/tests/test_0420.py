import keras
import matplotlib.pyplot as plt
import numpy as np
import pytest
from src_0420 import task_func


@pytest.fixture
def sample_data():
    np.random.seed(0)
    X = np.random.rand(100, 5)
    Y = np.random.randint(0, 2, 100)
    return X, Y

def test_task_func_output(sample_data):
    X, Y = sample_data
    model, ax = task_func(X, Y)
    
    assert isinstance(model, keras.Model), "The first output should be a Keras model"
    assert isinstance(ax, plt.Axes), "The second output should be a matplotlib Axes object"

def test_model_input_shape(sample_data):
    X, Y = sample_data
    model, _ = task_func(X, Y)
    input_layer = model.layers[0]
    assert input_layer.input_shape == (None, X.shape[1]), "Input shape of the model does not match the input data"

def test_model_output_shape(sample_data):
    X, Y = sample_data
    model, _ = task_func(X, Y)
    output_layer = model.layers[-1]
    assert output_layer.output_shape == (None, 1), "Output shape of the model should be (None, 1)"

def test_precision_recall_curve(sample_data):
    X, Y = sample_data
    _, ax = task_func(X, Y)
    lines = ax.get_lines()
    assert len(lines) == 1, "There should be only one line in the plot"
    assert lines[0].get_label() == 'Precision-Recall curve', "The plot should have a Precision-Recall curve labeled correctly"

def test_plot_labels(sample_data):
    X, Y = sample_data
    _, ax = task_func(X, Y)
    assert ax.get_xlabel() == 'Recall', "X-axis label should be 'Recall'"
    assert ax.get_ylabel() == 'Precision', "Y-axis label should be 'Precision'"
    assert ax.get_title() == 'Precision-Recall Curve', "Plot title should be 'Precision-Recall Curve'"

def test_legend_location(sample_data):
    X, Y = sample_data
    _, ax = task_func(X, Y)
    legend = ax.get_legend()
    assert legend.get_loc() == 'best', "Legend location should be 'best'"