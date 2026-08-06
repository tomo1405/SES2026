import pytest
from src_1088 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def test_task_func():
    # Test 1: Test that the function returns the correct values for skewness and kurtosis
    mean = 123456.908
    std_dev = 1.2
    skewness, kurtosis, plot_paths = task_func(mean, std_dev)
    assert skewness == stats.skew(np.random.normal(mean, std_dev, 1000))
    assert kurtosis == stats.kurtosis(np.random.normal(mean, std_dev, 1000))

    # Test 2: Test that the function saves the plots correctly
    mean = 123456.908
    std_dev = 1.2
    skewness, kurtosis, plot_paths = task_func(mean, std_dev, save_plots=True)
    assert len(plot_paths) == 2
    assert "histogram_plot.png" in plot_paths
    assert "qq_plot.png" in plot_paths

    # Test 3: Test that the function raises an error if the mean and std_dev are not provided
    with pytest.raises(TypeError):
        task_func()

    # Test 4: Test that the function raises an error if the mean is not a number
    with pytest.raises(TypeError):
        task_func("mean", 1.2)

    # Test 5: Test that the function raises an error if the std_dev is not a number
    with pytest.raises(TypeError):
        task_func(123456.908, "std_dev")

    # Test 6: Test that the function raises an error if the save_plots is not a boolean
    with pytest.raises(TypeError):
        task_func(123456.908, 1.2, save_plots="True")