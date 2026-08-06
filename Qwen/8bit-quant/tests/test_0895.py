import pytest
from src_0895 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Call the function
    array, mean, std, ax = task_func()
    
    # Check if the array has the correct size
    assert len(array) == 10000
    
    # Check if the mean and std are calculated correctly
    calculated_mean = np.mean(array)
    calculated_std = np.std(array)
    assert np.isclose(mean, calculated_mean)
    assert np.isclose(std, calculated_std)
    
    # Check if the plot is created with the correct title and labels
    assert ax.get_title() == 'Histogram of Random Integers'
    assert ax.get_xlabel() == 'Value'
    assert ax.get_ylabel() == 'Frequency'
    
    # Check if the vertical lines are drawn at the correct positions
    lines = ax.get_lines()
    assert len(lines) == 3
    assert np.isclose(lines[0].get_xdata()[0], mean)
    assert np.isclose(lines[1].get_xdata()[0], mean + std)
    assert np.isclose(lines[2].get_xdata()[0], mean - std)
    
    # Check if the legend is correct
    legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
    assert legend_labels == ["Mean", "Standard Deviation", "Standard Deviation"]

# To run the tests, you can use the command: pytest -v