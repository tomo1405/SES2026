import pytest
from src_0911 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Test case 1: Basic functionality
    letters = ['A', 'B', 'C']
    repetitions = [3, 2, 1]
    colors = ['red', 'green', 'blue']
    expected_counts = np.array([3, 2, 1])
    
    fig, ax = task_func(letters, repetitions, colors)
    
    # Check if the plot is created without errors
    assert plt.gcf() is not None
    
    # Add more assertions to check the plot content if necessary

    # Clean up the plot to avoid polluting the global namespace
    plt.close()

    # Add more test cases as needed

# Add more test cases as needed