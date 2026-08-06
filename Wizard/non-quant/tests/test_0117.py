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
    # Test case 1
    mu = 0
    sigma = 1
    sample_size = 1000
    samples = task_func(mu, sigma, sample_size)
    assert len(samples) == sample_size
    assert np.mean(samples) == pytest.approx(mu, abs=0.1)
    assert np.std(samples) == pytest.approx(sigma, abs=0.1)
    
    # Test case 2
    mu = 10
    sigma = 2
    sample_size = 500
    samples = task_func(mu, sigma, sample_size)
    assert len(samples) == sample_size
    assert np.mean(samples) == pytest.approx(mu, abs=0.1)
    assert np.std(samples) == pytest.approx(sigma, abs=0.1)