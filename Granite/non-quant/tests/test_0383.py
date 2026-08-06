import matplotlib.pyplot as plt
import numpy as np
import pytest
from src_0383 import task_func


def test_task_func():
    # Test case 1: Test with length = 1000
    distribution, ax = task_func(1000)
    assert isinstance(distribution, np.ndarray)
    assert isinstance(ax, plt.Axes)
    
    # Test case 2: Test with length = 500
    distribution, ax = task_func(500)
    assert isinstance(distribution, np.ndarray)
    assert isinstance(ax, plt.Axes)
    
    # Test case 3: Test with invalid length (string)
    with pytest.raises(TypeError):
        distribution, ax = task_func("invalid")