import pytest
from src_0655 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Test case where there are enough points for fitting
    array = np.array([[1, 2], [1, 3], [1, 4], [2, 5]])
    target_value = 1
    popt, ax = task_func(array, target_value)
    
    assert isinstance(popt, np.ndarray)
    assert len(popt) == 3
    assert isinstance(ax, plt.Axes)

    # Test case where there are not enough points for fitting
    with pytest.raises(ValueError):
        array = np.array([[1, 2], [1, 3]])
        task_func(array, 1)

    # Test case with different target value
    array = np.array([[1, 2], [2, 3], [2, 4], [2, 5], [3, 6]])
    target_value = 2
    popt, ax = task_func(array, target_value)
    
    assert isinstance(popt, np.ndarray)
    assert len(popt) == 3
    assert isinstance(ax, plt.Axes)