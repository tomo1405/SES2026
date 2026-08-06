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
    # Test case 1: sample_size is an integer
    assert isinstance(task_func(0, 1, 10), np.ndarray)
    
    # Test case 2: mu is a float
    assert isinstance(task_func(0.5, 1, 10), np.ndarray)
    
    # Test case 3: sigma is a float
    assert isinstance(task_func(0, 0.5, 10), np.ndarray)
    
    # Test case 4: sample_size is a float
    with pytest.raises(TypeError):
        task_func(0, 1, 10.5)
    
    # Test case 5: mu is a string
    with pytest.raises(TypeError):
        task_func('a', 1, 10)
    
    # Test case 6: sigma is a string
    with pytest.raises(TypeError):
        task_func(0, 'b', 10)