import pytest
from src_0117 import task_func
import numpy as np
import io
import matplotlib.pyplot as plt

# Mocking plt.show to prevent actual plotting
plt.show = lambda: None

def test_task_func():
    mu = 0
    sigma = 1
    sample_size = 1000
    
    # Capture the output to check if the function runs without errors
    with io.StringIO() as buf, pytest.MonkeyPatch().context() as mp:
        mp.setattr(plt, 'savefig', lambda x: buf.write("Saved plot to " + x))
        samples = task_func(mu, sigma, sample_size)
    
    # Check if the returned samples have the correct shape
    assert samples.shape == (sample_size,)
    
    # Check if the mean and standard deviation are close to the expected values
    assert np.isclose(np.mean(samples), mu, atol=0.1)
    assert np.isclose(np.std(samples), sigma, atol=0.1)

def test_task_func_with_different_parameters():
    mu = 5
    sigma = 2
    sample_size = 500
    
    # Capture the output to check if the function runs without errors
    with io.StringIO() as buf, pytest.MonkeyPatch().context() as mp:
        mp.setattr(plt, 'savefig', lambda x: buf.write("Saved plot to " + x))
        samples = task_func(mu, sigma, sample_size)
    
    # Check if the returned samples have the correct shape
    assert samples.shape == (sample_size,)
    
    # Check if the mean and standard deviation are close to the expected values
    assert np.isclose(np.mean(samples), mu, atol=0.2)
    assert np.isclose(np.std(samples), sigma, atol=0.2)