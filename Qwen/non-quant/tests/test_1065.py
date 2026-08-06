import pytest
from src_1065 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Create a sample 2D array
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    
    # Call the function
    ax = task_func(arr)
    
    # Check if the returned object is an AxesSubplot
    assert isinstance(ax, plt.Axes), "The function should return an AxesSubplot object"
    
    # Check if the title is set correctly
    assert ax.get_title() == "Heatmap of the 2D Array", "The title of the heatmap is incorrect"
    
    # Check if the heatmap data is correct
    heatmap_data = ax.collections[0].get_array()
    assert np.array_equal(heatmap_data, arr.ravel()), "The heatmap data does not match the input array"
    
    # Check if vmin and vmax are set correctly
    assert ax.collections[0].get_clim()[0] == np.min(arr), "vmin is not set correctly"
    assert ax.collections[0].get_clim()[1] == np.max(arr), "vmax is not set correctly"

# To run the tests, use the command: pytest -v