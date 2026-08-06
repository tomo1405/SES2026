import matplotlib.pyplot as plt
import numpy as np
from src_0895 import task_func


def test_task_func():
    array, mean, std, ax = task_func()
    
    # Test the return type of the function
    assert isinstance(array, np.ndarray)
    assert isinstance(mean, float)
    assert isinstance(std, float)
    assert isinstance(ax, plt.Axes)
    
    # Test the values of the mean and standard deviation
    assert mean == np.mean(array)
    assert std == np.std(array)
    
    # Test the title, x-label, and y-label of the histogram
    assert ax.get_title() == 'Histogram of Random Integers'
    assert ax.get_xlabel() == 'Value'
    assert ax.get_ylabel() == 'Frequency'
    
    # Test the presence of the mean and standard deviation lines
    assert len(ax.get_lines()) == 4
    assert ax.get_lines()[2].get_color() == 'red'
    assert ax.get_lines()[2].get_linestyle() == 'dashed'
    assert ax.get_lines()[2].get_linewidth() == 1
    assert ax.get_lines()[3].get_color() == 'purple'
    assert ax.get_lines()[3].get_linestyle() == 'dashed'
    assert ax.get_lines()[3].get_linewidth() == 1
    assert ax.get_lines()[3].get_linestyle() == 'dashed'
    assert ax.get_lines()[3].get_linewidth() == 1
    
    # Test the legend
    assert ax.get_legend().get_texts()[0].get_text() == 'Mean'
    assert ax.get_legend().get_texts()[1].get_text() == 'Standard Deviation'