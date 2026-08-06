import pytest
from src_0215 import task_func
import numpy as np

def test_task_func_default_parameters():
    ax, image = task_func()
    assert image.shape == (100, 100, 3)
    assert image.dtype == np.uint8
    assert np.min(image) >= 0
    assert np.max(image) <= 255

def test_task_func_custom_seed():
    ax1, image1 = task_func(seed=123)
    ax2, image2 = task_func(seed=123)
    assert np.array_equal(image1, image2)

def test_task_func_custom_image_size():
    ax, image = task_func(image_size=(50, 50, 3))
    assert image.shape == (50, 50, 3)

def test_task_func_custom_range():
    ax, image = task_func(range_low=50, range_high=150)
    assert np.min(image) >= 50
    assert np.max(image) <= 150

def test_task_func_invalid_range():
    with pytest.raises(ValueError):
        task_func(range_low=200, range_high=100)