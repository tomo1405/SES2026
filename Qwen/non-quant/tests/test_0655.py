import pytest
from src_0655 import task_func
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_array():
    return np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])

@pytest.fixture
def target_value():
    return 2

def test_task_func_with_valid_input(sample_array, target_value):
    popt, ax = task_func(sample_array, target_value)
    assert isinstance(popt, np.ndarray)
    assert len(popt) == 3
    assert isinstance(ax, plt.Axes)

def test_task_func_with_insufficient_points():
    array = np.array([[1, 2], [2, 3]])
    target_value = 2
    with pytest.raises(ValueError, match="Not enough points to perform the fitting."):
        task_func(array, target_value)

def test_task_func_with_no_matching_points():
    array = np.array([[1, 2], [2, 3]])
    target_value = 5
    with pytest.raises(ValueError, match="Not enough points to perform the fitting."):
        task_func(array, target_value)