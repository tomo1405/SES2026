import pytest
from src_0471 import task_func
import matplotlib.pyplot as plt
import numpy as np

def test_task_func():
    # Test with a simple list of integers
    myList = [1, 2, 2, 3, 3, 3, 4]
    ax = task_func(myList)
    
    # Check if the axes object is created correctly
    assert isinstance(ax, plt.Axes)
    
    # Check if the histogram data is correct
    n, bins, patches = ax.hist(myList, bins=np.arange(min(myList), max(myList) + 2) - 0.5, edgecolor="black")
    expected_n = np.array([1, 2, 3, 1])
    assert np.array_equal(n, expected_n)
    
    # Check if the x and y labels are set correctly
    assert ax.get_xlabel() == "Value"
    assert ax.get_ylabel() == "Frequency"
    
    # Check if the title is set correctly
    assert ax.get_title() == "Histogram of Values"

# To run the tests, use the following command in your terminal:
# pytest <filename>.py