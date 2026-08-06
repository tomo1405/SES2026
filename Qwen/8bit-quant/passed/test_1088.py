import pytest
from src_1088 import task_func
import numpy as np

def test_task_func_default_values():
    skewness, kurtosis, plot_paths = task_func()
    assert isinstance(skewness, float)
    assert isinstance(kurtosis, float)
    assert isinstance(plot_paths, list)
    assert len(plot_paths) == 0

def test_task_func_save_plots():
    skewness, kurtosis, plot_paths = task_func(save_plots=True)
    assert isinstance(skewness, float)
    assert isinstance(kurtosis, float)
    assert isinstance(plot_paths, list)
    assert len(plot_paths) == 2
    assert "histogram_plot.png" in plot_paths
    assert "qq_plot.png" in plot_paths

def test_task_func_custom_mean_std_dev():
    mean = 100000
    std_dev = 0.5
    skewness, kurtosis, plot_paths = task_func(mean=mean, std_dev=std_dev)
    assert isinstance(skewness, float)
    assert isinstance(kurtosis, float)
    assert isinstance(plot_paths, list)
    assert len(plot_paths) == 0

def test_task_func_negative_mean():
    mean = -123456.908
    skewness, kurtosis, plot_paths = task_func(mean=mean)
    assert isinstance(skewness, float)
    assert isinstance(kurtosis, float)
    assert isinstance(plot_paths, list)
    assert len(plot_paths) == 0

def test_task_func_large_std_dev():
    std_dev = 100
    skewness, kurtosis, plot_paths = task_func(std_dev=std_dev)
    assert isinstance(skewness, float)
    assert isinstance(kurtosis, float)
    assert isinstance(plot_paths, list)
    assert len(plot_paths) == 0

def test_task_func_small_std_dev():
    std_dev = 0.01
    skewness, kurtosis, plot_paths = task_func(std_dev=std_dev)
    assert isinstance(skewness, float)
    assert isinstance(kurtosis, float)
    assert isinstance(plot_paths, list)
    assert len(plot_paths) == 0