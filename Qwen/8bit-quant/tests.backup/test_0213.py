import pytest
from src_0213 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Test with a simple dataset
    data = [(1, 2), (3, 4), (5, 6)]
    ax, max_y_point = task_func(data)
    
    # Check if the max_y_point is correct
    assert max_y_point == (5, 6)
    
    # Check if the plot has the correct number of points
    lines = ax.get_lines()
    scatter_plots = ax.collections
    
    assert len(scatter_plots) == 2  # One for all points, one for the max point
    
    # Check if the labels are set correctly
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'
    assert ax.get_title() == 'Points with Max Y Point Highlighted'
    
    # Check if the legend is present
    legend = ax.get_legend()
    assert legend is not None
    assert len(legend.get_texts()) == 2  # One for each label
    
    # Clean up the plot to avoid interference with other tests
    plt.close(fig)

# Test with an empty dataset
def test_task_func_empty_data():
    data = []
    with pytest.raises(ValueError):  # Assuming max() on empty list raises ValueError
        task_func(data)

# Test with a dataset where all y values are the same
def test_task_func_same_y_values():
    data = [(1, 2), (3, 2), (5, 2)]
    ax, max_y_point = task_func(data)
    
    # Check if the max_y_point is the first point (or any point, since they are all equal)
    assert max_y_point == (1, 2)
    
    # Clean up the plot
    plt.close(fig)