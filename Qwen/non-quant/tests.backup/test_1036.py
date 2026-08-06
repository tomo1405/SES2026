import pytest
from src_1036 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    feature = pd.Series(np.random.randint(0, 2, size=100))
    target = pd.Series(np.random.randint(0, 2, size=100))
    return feature, target

def test_task_func_output_type(sample_data):
    feature, target = sample_data
    cm, ax = task_func(feature, target)
    assert isinstance(cm, np.ndarray)
    assert isinstance(ax, plt.Axes)

def test_task_func_confusion_matrix_shape(sample_data):
    feature, target = sample_data
    cm, _ = task_func(feature, target)
    assert cm.shape == (2, 2)

def test_task_func_plot_labels(sample_data):
    feature, target = sample_data
    _, ax = task_func(feature, target)
    assert ax.get_xlabel() == "Predicted"
    assert ax.get_ylabel() == "Actual"
    assert ax.get_xticklabels()[1].get_text() == "Yes"
    assert ax.get_yticklabels()[1].get_text() == "Yes"

def test_task_func_plot_title(sample_data):
    feature, target = sample_data
    _, ax = task_func(feature, target)
    assert ax.get_title() == "Confusion Matrix"

def test_task_func_plot_colorbar(sample_data):
    feature, target = sample_data
    _, ax = task_func(feature, target)
    cax = ax.images[0]
    assert cax.colorbar is not None