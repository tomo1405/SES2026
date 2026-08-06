import pytest
from src_1067 import task_func
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def setup():
    plt.ioff()  # Turn off interactive plotting
    yield
    plt.ion()  # Turn on interactive plotting

def test_task_func_default_parameters(setup):
    data, outliers_detected, ax = task_func()
    assert len(data) == NUM_SAMPLES + NUM_OUTLIERS
    assert isinstance(data, np.ndarray)
    assert isinstance(outliers_detected, np.ndarray)
    assert isinstance(ax, plt.Axes)

def test_task_func_custom_parameters(setup):
    num_samples = 50
    num_outliers = 10
    data, outliers_detected, ax = task_func(num_samples, num_outliers)
    assert len(data) == num_samples + num_outliers
    assert isinstance(data, np.ndarray)
    assert isinstance(outliers_detected, np.ndarray)
    assert isinstance(ax, plt.Axes)

def test_task_func_no_normal_data(setup):
    num_samples = 0
    num_outliers = 10
    data, outliers_detected, ax = task_func(num_samples, num_outliers)
    assert len(data) == num_outliers
    assert isinstance(data, np.ndarray)
    assert isinstance(outliers_detected, np.ndarray)
    assert isinstance(ax, plt.Axes)

def test_task_func_all_outliers_detected(setup):
    num_samples = 10
    num_outliers = 10
    data, outliers_detected, ax = task_func(num_samples, num_outliers)
    assert len(data) == num_samples + num_outliers
    assert len(outliers_detected) > 0
    assert isinstance(data, np.ndarray)
    assert isinstance(outliers_detected, np.ndarray)
    assert isinstance(ax, plt.Axes)