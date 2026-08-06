import pytest
from src_1067 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_default():
    data, outliers_detected, ax = task_func()
    assert len(data) == 105
    assert len(outliers_detected) <= 5
    assert isinstance(ax, plt.Axes)

def test_task_func_no_normal_data():
    data, outliers_detected, ax = task_func(num_samples=0)
    assert len(data) == 5
    assert len(outliers_detected) == 5
    assert isinstance(ax, plt.Axes)

def test_task_func_custom_samples_and_outliers():
    num_samples = 200
    num_outliers = 10
    data, outliers_detected, ax = task_func(num_samples=num_samples, num_outliers=num_outliers)
    assert len(data) == num_samples + num_outliers
    assert len(outliers_detected) <= num_outliers
    assert isinstance(ax, plt.Axes)

def test_task_func_no_outliers():
    num_samples = 1000
    num_outliers = 0
    data, outliers_detected, ax = task_func(num_samples=num_samples, num_outliers=num_outliers)
    assert len(data) == num_samples
    assert len(outliers_detected) == 0
    assert isinstance(ax, plt.Axes)

def test_task_func_large_outliers():
    num_samples = 100
    num_outliers = 50
    data, outliers_detected, ax = task_func(num_samples=num_samples, num_outliers=num_outliers)
    assert len(data) == num_samples + num_outliers
    assert len(outliers_detected) <= num_outliers
    assert isinstance(ax, plt.Axes)

def test_task_func_negative_samples():
    with pytest.raises(ValueError):
        task_func(num_samples=-10)

def test_task_func_negative_outliers():
    with pytest.raises(ValueError):
        task_func(num_outliers=-5)