import pytest
from src_0895 import task_func
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def setup_test():
    # Mocking the plot show function to prevent actual plotting
    plt.show = lambda: None
    return task_func()

def test_task_func_output(setup_test):
    array, mean, std, ax = setup_test
    
    # Check if the array has the correct size
    assert len(array) == 10000
    
    # Check if the array contains integers between 1 and 100
    assert np.all(array >= 1) and np.all(array <= 100)
    
    # Check if the mean is calculated correctly
    assert np.isclose(mean, np.mean(array))
    
    # Check if the standard deviation is calculated correctly
    assert np.isclose(std, np.std(array))
    
    # Check if the axes object is created correctly
    assert isinstance(ax, plt.Axes)
    
    # Check if the histogram is plotted correctly
    assert len(ax.lines) == 3  # Mean and two standard deviations lines
    assert len(ax.patches) > 0  # Histogram bars
    
    # Check if the legend is set correctly
    assert ax.get_legend().get_texts()[0].get_text() == "Mean"
    assert ax.get_legend().get_texts()[1].get_text() == "Standard Deviation"
    
    # Check if the axis labels and title are set correctly
    assert ax.get_xlabel() == 'Value'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.get_title() == 'Histogram of Random Integers'