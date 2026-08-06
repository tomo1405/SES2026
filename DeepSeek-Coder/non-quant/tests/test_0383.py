import pytest
from src_0383 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def test_task_func():
    # Generate a sample distribution
    length = 1000
    distribution, _ = task_func(length)
    
    # Check if the distribution is a numpy array
    assert isinstance(distribution, np.ndarray), "The distribution should be a numpy array"
    
    # Check if the length of the distribution is equal to the specified length
    assert len(distribution) == length, "The length of the distribution should be equal to the specified length"
    
    # Check if the histogram matches the expected distribution
    fig, ax = plt.subplots()
    ax.hist(distribution, 30, density=True, label='Histogram')
    ax.plot(np.sort(distribution), norm.pdf(np.sort(distribution), MU, SIGMA), 
             linewidth=2, color='r', label='PDF')
    ax.legend()
    
    # Add more assertions to check the plot
    plt.show()