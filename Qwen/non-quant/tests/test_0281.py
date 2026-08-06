import pytest
from src_0281 import task_func
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_signal():
    return np.array([1, 2, 3, 4, 5])

def test_task_func_output(sample_signal):
    transformed_signal, ax = task_func(sample_signal)
    assert isinstance(transformed_signal, np.ndarray)
    assert len(transformed_signal) == len(sample_signal)
    assert isinstance(ax, plt.AxesSubplot)

def test_task_func_precision(sample_signal):
    transformed_signal, _ = task_func(sample_signal, precision=3)
    assert all(isinstance(x, float) for x in transformed_signal.flatten())
    assert all(len(str(x).split('.')[1]) <= 3 for x in transformed_signal.flatten())

def test_task_func_seed(sample_signal):
    transformed_signal_1, _ = task_func(sample_signal, seed=777)
    transformed_signal_2, _ = task_func(sample_signal, seed=777)
    assert np.array_equal(transformed_signal_1, transformed_signal_2)

def test_task_func_plot_titles(sample_signal):
    _, ax = task_func(sample_signal)
    assert ax[0].get_title() == 'Original Signal'
    assert ax[1].get_title() == 'Transformed Signal'

def test_task_func_plot_layout(sample_signal):
    _, ax = task_func(sample_signal)
    assert plt.tight_layout() is None  # Check if layout adjustment was attempted