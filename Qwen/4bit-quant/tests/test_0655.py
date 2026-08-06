import pytest
from src_0655 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Create a sample array and target value
    array = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
    target_value = 3

    # Call the function
    popt, ax = task_func(array, target_value)

    # Check that the returned parameters are of the correct type
    assert isinstance(popt, np.ndarray)
    assert len(popt) == 3

    # Check that the plot is correctly created
    assert isinstance(ax, plt.Axes)

def test_task_func_not_enough_points():
    # Create an array with less than 3 points for the target value
    array = np.array([[1, 2], [2, 3]])
    target_value = 3

    # Check that a ValueError is raised
    with pytest.raises(ValueError, match="Not enough points to perform the fitting."):
        task_func(array, target_value)