import pytest
from src_1067 import task_func
import numpy as np

def test_task_func():
    # Test with default parameters
    data, outliers_detected, ax = task_func()
    assert isinstance(data, np.ndarray)
    assert isinstance(outliers_detected, np.ndarray)
    assert isinstance(ax, plt.Axes)
    assert len(data) == 100
    assert len(outliers_detected) == 5
    assert ax.get_xlabel() == 'Data'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.get_title() == 'Histogram of Data'

    # Test with custom parameters
    data, outliers_detected, ax = task_func(num_samples=50, num_outliers=10)
    assert isinstance(data, np.ndarray)
    assert isinstance(outliers_detected, np.ndarray)
    assert isinstance(ax, plt.Axes)
    assert len(data) == 50
    assert len(outliers_detected) == 10
    assert ax.get_xlabel() == 'Data'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.get_title() == 'Histogram of Data'

    # Test with no normal data
    data, outliers_detected, ax = task_func(num_samples=0, num_outliers=10)
    assert isinstance(data, np.ndarray)
    assert isinstance(outliers_detected, np.ndarray)
    assert isinstance(ax, plt.Axes)
    assert len(data) == 0
    assert len(outliers_detected) == 10
    assert ax.get_xlabel() == 'Data'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.get_title() == 'Histogram of Data'