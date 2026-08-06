import pytest
from src_0210 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Create some sample data
    data = [(1, 2), (3, 4), (5, 6)]
    
    # Call the function
    ax = task_func(data)
    
    # Check if the returned object is an AxesSubplot instance
    assert isinstance(ax, plt.Axes)
    
    # Check if the max tuple is correctly identified and plotted
    max_tuple = max(data, key=lambda x: x[1])
    assert max_tuple == (5, 6)
    
    # Check if the plot has the correct number of points
    lines, labels = ax.get_legend_handles_labels()
    assert len(lines) == 2  # One for the data, one for the max tuple
    
    # Check if the labels are correct
    assert 'Data' in labels
    assert 'Max Tuple' in labels
    
    # Check if the max tuple is highlighted in red
    scatter_points = ax.collections[1].get_offsets()
    assert scatter_points[0] == max_tuple
    
    # Check if the plot has the correct title and labels
    assert ax.get_title() == 'Max Tuple Highlighted'
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'

# Run the test
if __name__ == "__main__":
    pytest.main()