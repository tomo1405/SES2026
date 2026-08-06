import pytest
from src_0236 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Test with default parameters
    ax = task_func(mu=0, sigma=1)
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib Axes object"
    
    # Test with custom parameters
    ax = task_func(mu=5, sigma=2, seed=42, num_samples=500, num_bins=20)
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib Axes object"
    
    # Test with zero sigma, which should raise a warning due to division by zero in the Gaussian plot
    with pytest.warns(RuntimeWarning):
        ax = task_func(mu=0, sigma=0)
    
    # Test with negative sigma, which is not physically meaningful but should still run
    ax = task_func(mu=0, sigma=-1)
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib Axes object"

# To run the tests, you can use the following command in your terminal:
# pytest -v