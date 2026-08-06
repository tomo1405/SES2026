import pytest
from src_0170 import task_func
import numpy as np

def test_task_func_input_type():
    with pytest.raises(TypeError):
        task_func([1, 2, 3])

def test_task_func_sigma_value():
    with pytest.raises(ValueError):
        task_func(np.array([[1, 2], [3, 4]]), sigma=-1)

def test_task_func_return_type():
    image = np.array([[1, 2], [3, 4]])
    ax, filtered_image = task_func(image)
    assert isinstance(ax, np.ndarray)
    assert isinstance(filtered_image, np.ndarray)

def test_task_func_output_shape():
    image = np.array([[1, 2], [3, 4]])
    _, filtered_image = task_func(image)
    assert filtered_image.shape == image.shape

def test_task_func_output_values():
    image = np.array([[1, 2], [3, 4]])
    _, filtered_image = task_func(image)
    assert not np.array_equal(image, filtered_image)