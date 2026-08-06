import pytest
from src_1062 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def test_task_func():
    # Create a sample array for testing
    np.random.seed(0)
    arr = np.random.rand(5, 5)

    # Call the function
    ax, result = task_func(arr)

    # Assertions to check the output
    assert isinstance(ax, plt.Axes), "The first return value should be an instance of plt.Axes"
    assert isinstance(result, np.ndarray), "The second return value should be a numpy array"
    assert len(result) == arr.shape[0], "The length of the result should match the number of rows in the input array"

    # Close the plot to avoid hanging plots in some environments
    plt.close()