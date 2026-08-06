import pytest
from src_0170 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

def test_task_func():
    # Test with a valid image
    image = np.random.rand(100, 100)
    sigma = 2
    ax, filtered_image = task_func(image, sigma)
    
    assert isinstance(ax, list), "Expected ax to be a list"
    assert len(ax) == 2, "Expected ax to have 2 elements"
    assert isinstance(ax[0], plt.Axes), "Expected ax[0] to be a matplotlib AxesSubplot"
    assert isinstance(ax[1], plt.Axes), "Expected ax[1] to be a matplotlib AxesSubplot"
    
    assert isinstance(filtered_image, np.ndarray), "Expected filtered_image to be a numpy array"
    assert filtered_image.shape == image.shape, "Expected filtered_image to have the same shape as the input image"

    # Add more assertions as needed to cover other aspects of the function's behavior

    # Add more tests as needed to cover different scenarios

    # Clean up the plot to avoid polluting the global state
    plt.close('all')