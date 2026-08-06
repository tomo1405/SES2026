import pytest
from src_1079 import task_func
import numpy as np
import io
import matplotlib.pyplot as plt

@pytest.fixture
def setup_plot():
    # Redirect plot output to a BytesIO object
    old_stdout = io.BytesIO()
    plt.ioff()  # Turn off interactive mode
    plt.switch_backend('Agg')  # Use non-interactive backend
    yield
    plt.close('all')
    plt.ion()  # Turn on interactive mode
    old_stdout.close()

def test_task_func_uniform_distribution(setup_plot):
    arr = np.array([1, 2, 3, 4, 5])
    uniform_distribution, ax = task_func(arr)
    assert uniform_distribution is True
    assert isinstance(ax, plt.Axes)

def test_task_func_non_uniform_distribution(setup_plot):
    arr = np.array([1, 2, 2, 3, 3, 3])
    uniform_distribution, ax = task_func(arr)
    assert uniform_distribution is False
    assert isinstance(ax, plt.Axes)

def test_task_func_empty_array(setup_plot):
    arr = np.array([])
    uniform_distribution, ax = task_func(arr)
    assert uniform_distribution is True
    assert isinstance(ax, plt.Axes)

def test_task_func_single_element(setup_plot):
    arr = np.array([42])
    uniform_distribution, ax = task_func(arr)
    assert uniform_distribution is True
    assert isinstance(ax, plt.Axes)