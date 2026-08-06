import pytest
from src_0170 import task_func
import numpy as np

def test_task_func():
    image = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    sigma = 2
    ax, filtered_image = task_func(image, sigma)
    assert isinstance(ax, np.ndarray)
    assert isinstance(filtered_image, np.ndarray)
    assert ax.shape == (1, 2)
    assert filtered_image.shape == (3, 3)
    assert np.allclose(filtered_image, np.array([[0.99999999, 1.99999999, 2.99999999], [3.99999999, 4.99999999, 5.99999999], [6.99999999, 7.99999999, 8.99999999]]))

def test_task_func_invalid_image():
    image = "invalid"
    sigma = 2
    with pytest.raises(TypeError):
        task_func(image, sigma)

def test_task_func_invalid_sigma():
    image = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    sigma = 0
    with pytest.raises(ValueError):
        task_func(image, sigma)