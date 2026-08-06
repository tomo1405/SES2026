import pytest
from src_0170 import task_func
import numpy as np

def test_task_func_type_error():
    image = np.array([[1, 2, 3], [4, 5, 6]])
    with pytest.raises(TypeError):
        task_func(image, sigma=2)

def test_task_func_value_error():
    image = np.array([[1, 2, 3], [4, 5, 6]])
    with pytest.raises(ValueError):
        task_func(image, sigma=0)

def test_task_func_return_type():
    image = np.array([[1, 2, 3], [4, 5, 6]])
    ax, filtered_image = task_func(image, sigma=2)
    assert isinstance(ax, plt.Axes)
    assert isinstance(filtered_image, np.ndarray)

def test_task_func_return_value():
    image = np.array([[1, 2, 3], [4, 5, 6]])
    ax, filtered_image = task_func(image, sigma=2)
    assert np.allclose(filtered_image, gaussian_filter(image, sigma=2))