import pytest
from src_0170 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_type_error():
    with pytest.raises(TypeError):
        task_func("not an array")

def test_task_func_value_error():
    with pytest.raises(ValueError):
        task_func(np.array([1, 2, 3]), sigma=-1)

def test_task_func_output():
    image = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    ax, filtered_image = task_func(image, sigma=1)
    
    assert isinstance(ax, np.ndarray)
    assert isinstance(filtered_image, np.ndarray)
    assert filtered_image.shape == image.shape

def test_task_func_plot_titles():
    image = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    ax, _ = task_func(image, sigma=1)
    
    assert ax[0].get_title() == 'Original'
    assert ax[1].get_title() == 'Filtered'

def test_task_func_plot_images():
    image = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    ax, _ = task_func(image, sigma=1)
    
    assert np.array_equal(ax[0].images[0].get_array(), image)
    # Note: Direct comparison of filtered images is not straightforward due to Gaussian filtering effects.
    # Further checks can be added if needed, such as comparing specific pixel values within expected ranges.