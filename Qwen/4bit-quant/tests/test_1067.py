import matplotlib.pyplot as plt
import numpy as np
import pytest
from src_1067 import task_func


def test_task_func_default_values():
    data, outliers_detected, ax = task_func()
    assert len(data) == NUM_SAMPLES + NUM_OUTLIERS
    assert isinstance(data, np.ndarray)
    assert isinstance(outliers_detected, np.ndarray)
    assert isinstance(ax, plt.Axes)

def test_task_func_custom_values():
    num_samples = 50
    num_outliers = 3
    data, outliers_detected, ax = task_func(num_samples, num_outliers)
    assert len(data) == num_samples + num_outliers
    assert isinstance(data, np.ndarray)
    assert isinstance(outliers_detected, np.ndarray)
    assert isinstance(ax, plt.Axes)

def test_task_func_no_normal_data():
    num_samples = 0
    num_outliers = 10
    data, outliers_detected, ax = task_func(num_samples, num_outliers)
    assert len(data) == num_outliers
    assert isinstance(data, np.ndarray)
    assert isinstance(outliers_detected, np.ndarray)
    assert isinstance(ax, plt.Axes)

def test_task_func_no_outliers():
    num_samples = 100
    num_outliers = 0
    data, outliers_detected, ax = task_func(num_samples, num_outliers)
    assert len(data) == num_samples
    assert isinstance(data, np.ndarray)
    assert isinstance(outliers_detected, np.ndarray)
    assert isinstance(ax, plt.Axes)

def test_task_func_no_samples_or_outliers():
    num_samples = 0
    num_outliers = 0
    with pytest.raises(AssertionError):
        task_func(num_samples, num_outliers)