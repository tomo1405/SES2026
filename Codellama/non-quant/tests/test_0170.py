import matplotlib.pyplot as plt
import numpy as np
import pytest
from src_0170 import task_func


def test_task_func_valid_input():
    image = np.random.rand(10, 10)
    ax, filtered_image = task_func(image, sigma=2)
    assert isinstance(ax, plt.Axes)
    assert isinstance(filtered_image, np.ndarray)
    assert filtered_image.shape == (10, 10)

def test_task_func_invalid_input():
    with pytest.raises(TypeError):
        task_func(1, sigma=2)
    with pytest.raises(ValueError):
        task_func(np.random.rand(10, 10), sigma=0)