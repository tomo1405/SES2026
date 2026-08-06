import numpy as np
import pytest
from src_0215 import task_func


def test_task_func():
    ax, image = task_func()
    assert ax is not None
    assert image is not None
    assert image.shape == (100, 100, 3)
    assert image.dtype == np.uint8
    assert (image >= 0).all() and (image <= 255).all()

def test_task_func_seed():
    ax1, image1 = task_func(seed=42)
    ax2, image2 = task_func(seed=42)
    assert (image1 == image2).all()

def test_task_func_range():
    with pytest.raises(ValueError):
        task_func(range_low=255, range_high=0)
    ax, image = task_func(range_low=100, range_high=200)
    assert (image >= 100).all() and (image <= 200).all()