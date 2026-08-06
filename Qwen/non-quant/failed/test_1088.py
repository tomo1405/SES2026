import pytest
from src_1088 import task_func
import numpy as np

def test_task_func_default_parameters():
    skewness, kurtosis, plot_paths = task_func()
    assert isinstance(skewness, float)
    assert isinstance(kurtosis, float)
    assert isinstance(plot_paths, list)
    assert len(plot_paths) == 0

def test_task_func_with_save_plots():
    skewness, kurtosis, plot_paths = task_func(save_plots=True)
    assert isinstance(skewness, float)
    assert isinstance(kurtosis, float)
    assert isinstance(plot_paths, list)
    assert len(plot_paths) == 2
    assert "histogram_plot.png" in plot_paths
    assert "qq_plot.png" in plot_paths

def test_task_func_custom_mean_and_std_dev():
    mean = 100000.0
    std_dev = 2.5
    skewness, kurtosis, plot_paths = task_func(mean=mean, std_dev=std_dev)
    assert isinstance(skewness, float)
    assert isinstance(kurtosis, float)
    assert isinstance(plot_paths, list)
    assert len(plot_paths) == 0

def test_task_func_skewness_and_kurtosis_values():
    np.random.seed(0)  # For reproducibility
    skewness, kurtosis, _ = task_func(mean=0, std_dev=1, save_plots=False)
    assert np.isclose(skewness, 0.04095057979288122, atol=1e-2)
    assert np.isclose(kurtosis, 2.971745443292536, atol=1e-2)

def test_task_func_plot_file_creation():
    skewness, kurtosis, plot_paths = task_func(save_plots=True)
    assert len(plot_paths) == 2
    for path in plot_paths:
        assert Path(path).is_file()