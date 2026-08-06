import pytest
from src_0477 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Sample data
    X = np.array([1, 2, 3, 4, 5])
    Y = np.array([2, 4, 6, 8, 10])

    # Expected parameters (a, b, c) for the quadratic function y = 2x^2 + 0x + 0
    expected_params = [2, 0, 0]

    # Call the function
    params, ax = task_func(X, Y)

    # Check if the parameters are close to the expected values
    assert np.allclose(params, expected_params, atol=1e-2), f"Parameters {params} do not match expected {expected_params}"

    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes), "The function did not return a valid Axes object"

    # Clean up the plot
    plt.close(fig)