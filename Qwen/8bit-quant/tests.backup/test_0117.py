import pytest
from src_0117 import task_func
import numpy as np
import io
import matplotlib.pyplot as plt

# Redirect stdout to capture print statements if any
import sys
stdout_backup = sys.stdout
sys.stdout = io.StringIO()

# Mocking the plt.show() to prevent GUI display during tests
plt.ioff()

def test_task_func():
    mu = 0
    sigma = 1
    sample_size = 1000
    
    # Capture the output of the function
    result = task_func(mu, sigma, sample_size)
    
    # Check if the result is a numpy array
    assert isinstance(result, np.ndarray), "The result should be a numpy array"
    
    # Check if the shape of the result matches the sample size
    assert result.shape == (sample_size,), f"The shape of the result should be ({sample_size},)"
    
    # Check if the mean of the result is close to mu
    assert np.isclose(np.mean(result), mu, atol=0.1), "The mean of the result should be close to mu"
    
    # Check if the standard deviation of the result is close to sigma
    assert np.isclose(np.std(result), sigma, atol=0.1), "The standard deviation of the result should be close to sigma"

# Restore stdout
sys.stdout = stdout_backup

# Enable plt.show() back
plt.ion()