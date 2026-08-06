import pytest
from src_1088 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def test_task_func_default_parameters():
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

def test_task_func_custom_mean_and_std_dev():
    mean = 98765.432
    std_dev = 2.4
    skewness, kurtosis, plot_paths = task_func(mean=mean, std_dev=std_dev, save_plots=False)
    assert isinstance(skewness, float)
    assert isinstance(kurtosis, float)
    assert isinstance(plot_paths, list)
    assert len(plot_paths) == 0

def test_task_func_no_plots():
    skewness, kurtosis, plot_paths = task_func(save_plots=False)
    assert isinstance(skewness, float)
    assert isinstance(kurtosis, float)
    assert isinstance(plot_paths, list)
    assert len(plot_paths) == 0

def test_task_func_skewness_and_kurtosis_values():
    skewness, kurtosis, _ = task_func()
    assert np.isclose(skewness, 0, atol=0.1)
    assert np.isclose(kurtosis, 0, atol=0.1)

def test_task_func_plot_files_exist():
    skewness, kurtosis, plot_paths = task_func(save_plots=True)
    for path in plot_paths:
        assert plt.imread(path) is not None, f"File {path} does not exist or is not readable"

# To run these tests, you can use the command: pytest -v