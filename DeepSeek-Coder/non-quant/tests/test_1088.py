import pytest
from src_1088 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def test_task_func():
    # Test with default parameters
    skewness, kurtosis, plot_paths = task_func()
    assert isinstance(skewness, float), "Skewness should be a float"
    assert isinstance(kurtosis, float), "Kurtosis should be a float"
    assert isinstance(plot_paths, list), "Plot paths should be a list"
    assert len(plot_paths) == 2, "Expected 2 plot paths"

    # Test with save_plots=True
    skewness, kurtosis, plot_paths = task_func(save_plots=True)
    assert isinstance(skewness, float), "Skewness should be a float"
    assert isinstance(kurtosis, float), "Kurtosis should be a float"
    assert isinstance(plot_paths, list), "Plot paths should be a list"
    assert len(plot_paths) == 2, "Expected 2 plot paths"

    # Test with invalid input
    with pytest.raises(TypeError):
        task_func("invalid_input")