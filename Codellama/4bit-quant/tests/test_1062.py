import pytest
from src_1062 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def test_task_func():
    # Test case 1: Testing with a valid input
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    ax, normalized_data = task_func(arr)
    assert isinstance(ax, plt.Axes)
    assert isinstance(normalized_data, np.ndarray)
    assert normalized_data.shape == (2,)
    assert np.allclose(normalized_data, np.array([1, 2]))

    # Test case 2: Testing with an invalid input
    with pytest.raises(ValueError):
        task_func(np.array([1, 2, 3]))

    # Test case 3: Testing the histogram plot
    ax, normalized_data = task_func(np.array([[1, 2, 3], [4, 5, 6]]))
    assert isinstance(ax, plt.Axes)
    assert isinstance(normalized_data, np.ndarray)
    assert normalized_data.shape == (2,)
    assert np.allclose(normalized_data, np.array([1, 2]))
    assert ax.get_title() == "Histogram of Normalized Data with Standard Normal PDF"
    assert ax.get_xlabel() == "Normalized Data"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_xlim() == (0, 1)
    assert ax.get_ylim() == (0, 1)

    # Test case 4: Testing the PDF plot
    ax, normalized_data = task_func(np.array([[1, 2, 3], [4, 5, 6]]))
    assert isinstance(ax, plt.Axes)
    assert isinstance(normalized_data, np.ndarray)
    assert normalized_data.shape == (2,)
    assert np.allclose(normalized_data, np.array([1, 2]))
    assert ax.get_title() == "Histogram of Normalized Data with Standard Normal PDF"
    assert ax.get_xlabel() == "Normalized Data"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_xlim() == (0, 1)
    assert ax.get_ylim() == (0, 1)
    assert ax.get_lines()[0].get_color() == "g"
    assert ax.get_lines()[0].get_linewidth() == 2
    assert ax.get_lines()[1].get_color() == "r"
    assert ax.get_lines()[1].get_linewidth() == 2