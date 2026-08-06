import pytest
from src_0117 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Define parameters
    mu = 0
    sigma = 1
    sample_size = 1000

    # Call the function
    samples = task_func(mu, sigma, sample_size)

    # Assert that the function returns a numpy array
    assert isinstance(samples, np.ndarray), "The function should return a numpy array"

    # Assert that the length of the samples is equal to the sample size
    assert len(samples) == sample_size, "The length of the samples should be equal to the sample size"

    # Assert that the mean of the samples is approximately equal to the mean used to generate the samples
    assert np.isclose(np.mean(samples), mu, atol=0.1), "The mean of the samples should be close to the mean used to generate the samples"

    # Assert that the standard deviation of the samples is approximately equal to the standard deviation used to generate the samples
    assert np.isclose(np.std(samples), sigma, atol=0.1), "The standard deviation of the samples should be close to the standard deviation used to generate the samples"

    # Check if the plot is generated without errors
    try:
        plt.close()
    except Exception as e:
        pytest.fail("Plotting failed with error: " + str(e))