python
import numpy as np
import matplotlib.pyplot as plt
import pytest

def task_func(mu, sigma, sample_size):
    samples = np.random.normal(mu, sigma, sample_size)
    
    # Plotting the histogram of the samples
    plt.hist(samples, bins=30, alpha=0.75, color='blue')
    plt.title('Histogram of Generated Samples')
    plt.xlabel('Sample values')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()
    
    return samples

def test_task_func():
    # Test case 1: Test with sample size 1000
    mu = 0
    sigma = 1
    sample_size = 1000
    samples = task_func(mu, sigma, sample_size)
    assert len(samples) == sample_size
    
    # Test case 2: Test with sample size 5000
    mu = 5
    sigma = 2
    sample_size = 5000
    samples = task_func(mu, sigma, sample_size)
    assert len(samples) == sample_size
    
    # Test case 3: Test with sample size 10000
    mu = -3
    sigma = 4
    sample_size = 10000
    samples = task_func(mu, sigma, sample_size)
    assert len(samples) == sample_size