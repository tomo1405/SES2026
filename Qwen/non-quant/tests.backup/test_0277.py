import pytest
from src_0277 import task_func
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

@pytest.fixture
def sample_matrix():
    return [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

def test_task_func_output(sample_matrix):
    skewness, kurtosis, ax = task_func(sample_matrix)
    
    # Check if the returned values are of correct type
    assert isinstance(skewness, float)
    assert isinstance(kurtosis, float)
    assert isinstance(ax, plt.AxesSubplot)
    
    # Calculate expected skewness and kurtosis
    max_values = [max(row) for row in sample_matrix]
    expected_skewness = stats.skew(max_values)
    expected_kurtosis = stats.kurtosis(max_values)
    
    # Assert that the calculated skewness and kurtosis match the expected values
    assert np.isclose(skewness, expected_skewness)
    assert np.isclose(kurtosis, expected_kurtosis)

def test_task_func_plot(sample_matrix):
    _, _, ax = task_func(sample_matrix)
    
    # Check if the plot has the correct number of lines (histogram + normal distribution curve)
    lines = ax.get_lines()
    assert len(lines) == 2
    
    # Check if the histogram is plotted correctly
    patches = ax.patches
    assert len(patches) == 10  # 10 bins
    
    # Check if the normal distribution curve is plotted correctly
    xdata, ydata = lines[1].get_data()
    assert len(xdata) == 100
    assert len(ydata) == 100

def test_task_func_with_empty_matrix():
    with pytest.raises(ValueError):
        task_func([])

def test_task_func_with_single_row_matrix():
    matrix = [[1, 2, 3]]
    skewness, kurtosis, ax = task_func(matrix)
    
    assert isinstance(skewness, float)
    assert isinstance(kurtosis, float)
    assert isinstance(ax, plt.AxesSubplot)
    
    max_values = [max(row) for row in matrix]
    expected_skewness = stats.skew(max_values)
    expected_kurtosis = stats.kurtosis(max_values)
    
    assert np.isclose(skewness, expected_skewness)
    assert np.isclose(kurtosis, expected_kurtosis)