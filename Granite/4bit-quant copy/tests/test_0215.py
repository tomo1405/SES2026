import pytest
import random
import numpy as np
import cv2
import matplotlib.pyplot as plt
from src_0215 import task_func

def test_task_func():
    seed = 42
    image_size = (100, 100, 3)
    range_low = 0
    range_high = 255
    ax, image = task_func(seed, image_size, range_low, range_high)
    assert ax is not None
    assert image is not None
    assert image.shape == image_size
    assert image.dtype == np.uint8
    assert np.all(image >= range_low) and np.all(image <= range_high)

def test_task_func_invalid_range():
    seed = 42
    image_size = (100, 100, 3)
    range_low = 255
    range_high = 0
    with pytest.raises(ValueError):
        task_func(seed, image_size, range_low, range_high)