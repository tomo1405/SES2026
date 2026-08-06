import pytest
from src_0218 import task_func
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def test_task_func():
    # Test with default parameters
    ax, mean, std = task_func()
    assert np.allclose(mean, 0)
    assert np.allclose(std, 1)
    assert ax.get_title() == "Normal Distribution with $\mu = 0, \sigma = 1$"
    assert ax.get_xlabel() == "Value"
    assert ax.get_ylabel() == "Frequency"
    assert len(ax.get_lines()) == 1
    assert ax.get_lines()[0].get_label() == "Sample Histogram"
    assert ax.get_lines()[0].get_color() == "b"
    assert ax.get_lines()[0].get_linewidth() == 2
    assert ax.get_lines()[0].get_linestyle() == "solid"
    assert len(ax.get_legend().get_texts()) == 1
    assert ax.get_legend().get_texts()[0].get_text() == "Sample Histogram"

    # Test with custom parameters
    ax, mean, std = task_func(mu=1, sigma=2, sample_size=1000, seed=0)
    assert np.allclose(mean, 1)
    assert np.allclose(std, 2)
    assert ax.get_title() == "Normal Distribution with $\mu = 1, \sigma = 2$"
    assert ax.get_xlabel() == "Value"
    assert ax.get_ylabel() == "Frequency"
    assert len(ax.get_lines()) == 1
    assert ax.get_lines()[0].get_label() == "Sample Histogram"
    assert ax.get_lines()[0].get_color() == "b"
    assert ax.get_lines()[0].get_linewidth() == 2
    assert ax.get_lines()[0].get_linestyle() == "solid"
    assert len(ax.get_legend().get_texts()) == 1
    assert ax.get_legend().get_texts()[0].get_text() == "Sample Histogram"

    # Test with custom parameters and custom seed
    ax, mean, std = task_func(mu=1, sigma=2, sample_size=1000, seed=1234)
    assert np.allclose(mean, 1)
    assert np.allclose(std, 2)
    assert ax.get_title() == "Normal Distribution with $\mu = 1, \sigma = 2$"
    assert ax.get_xlabel() == "Value"
    assert ax.get_ylabel() == "Frequency"
    assert len(ax.get_lines()) == 1
    assert ax.get_lines()[0].get_label() == "Sample Histogram"
    assert ax.get_lines()[0].get_color() == "b"
    assert ax.get_lines()[0].get_linewidth() == 2
    assert ax.get_lines()[0].get_linestyle() == "solid"
    assert len(ax.get_legend().get_texts()) == 1
    assert ax.get_legend().get_texts()[0].get_text() == "Sample Histogram"