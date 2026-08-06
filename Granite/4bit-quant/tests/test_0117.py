import pytest
from src_0117 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Test case 1: Check if the function returns the expected output for a given input
    mu = 0
    sigma = 1
    sample_size = 1000
    expected_output = np.random.normal(mu, sigma, sample_size)
    output = task_func(mu, sigma, sample_size)
    assert np.array_equal(output, expected_output)
    
    # Test case 2: Check if the histogram plot is displayed correctly
    mu = 5
    sigma = 2
    sample_size = 1000
    expected_output = np.random.normal(mu, sigma, sample_size)
    output = task_func(mu, sigma, sample_size)
    assert isinstance(output, np.ndarray)
    assert len(output) == sample_size
    plt.close()  # Close the plot window to avoid affecting other tests
    
    # Test case 3: Check if the function raises an error for invalid input
    with pytest.raises(ValueError):
        task_func('invalid_input', 1, 1)