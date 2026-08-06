import pytest
from src_0383 import task_func

def test_task_func():
    # Test case 1: length = 100
    distribution, ax = task_func(100)
    assert isinstance(distribution, np.ndarray)
    assert isinstance(ax, plt.Axes)
    assert distribution.shape == (100,)
    
    # Test case 2: length = 50
    distribution, ax = task_func(50)
    assert isinstance(distribution, np.ndarray)
    assert isinstance(ax, plt.Axes)
    assert distribution.shape == (50,)
    
    # Test case 3: length = 200
    distribution, ax = task_func(200)
    assert isinstance(distribution, np.ndarray)
    assert isinstance(ax, plt.Axes)
    assert distribution.shape == (200,)