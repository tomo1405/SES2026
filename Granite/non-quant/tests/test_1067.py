import numpy as np
import matplotlib.pyplot as plt
from src_1067 import task_func
import pytest

def test_task_func():
    num_samples = 100
    num_outliers = 5
    data, outliers_detected, ax = task_func(num_samples, num_outliers)
    assert isinstance(data, np.ndarray)
    assert isinstance(outliers_detected, np.ndarray)
    assert isinstance(ax, plt.Axes)
    assert len(data) == num_samples + num_outliers
    if num_samples > 0:
        assert len(outliers_detected) == num_outliers
    else:
        assert len(outliers_detected) == num_samples + num_outliers
    assert ax.get_xlabel() == 'Values'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.get_title() == 'Histogram of Data'

def test_task_func_with_no_outliers():
    num_samples = 100
    num_outliers = 0
    data, outliers_detected, ax = task_func(num_samples, num_outliers)
    assert isinstance(data, np.ndarray)
    assert isinstance(outliers_detected, np.ndarray)
    assert isinstance(ax, plt.Axes)
    assert len(data) == num_samples + num_outliers
    assert len(outliers_detected) == num_outliers
    assert ax.get_xlabel() == 'Values'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.get_title() == 'Histogram of Data'

def test_task_func_with_no_samples():
    num_samples = 0
    num_outliers = 5
    data, outliers_detected, ax = task_func(num_samples, num_outliers)
    assert isinstance(data, np.ndarray)
    assert isinstance(outliers_detected, np.ndarray)
    assert isinstance(ax, plt.Axes)
    assert len(data) == num_samples + num_outliers
    assert len(outliers_detected) == num_samples + num_outliers
    assert ax.get_xlabel() == 'Values'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.get_title() == 'Histogram of Data'