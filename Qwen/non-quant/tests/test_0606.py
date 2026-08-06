import pytest
from src_0606 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Create a sample matrix
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    
    # Call the function
    ax = task_func(matrix)
    
    # Check if the returned object is an AxesSubplot
    assert isinstance(ax, plt.Axes), "The function should return an AxesSubplot object"
    
    # Check if the data in the AxesSubplot matches the input matrix
    image_data = ax.images[0].get_array()
    assert np.array_equal(image_data, matrix), "The image data in the AxesSubplot does not match the input matrix"
    
    # Check if the colormap is set to 'hot'
    assert ax.images[0].get_cmap().name == 'hot', "The colormap should be set to 'hot'"
    
    # Check if the interpolation is set to 'nearest'
    assert ax.images[0].get_interpolation() == 'nearest', "The interpolation should be set to 'nearest'"

# To run the tests, use the command: pytest <filename>.py