import pytest
from src_0623 import task_func
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from itertools import chain

def test_task_func():
    # Create a sample list of lists for testing
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = task_func(data)
    
    # Assert that the function runs without errors and returns a matplotlib Axes object
    assert result is not None
    assert isinstance(result, plt.Axes)

    # Close the plot to avoid hanging tests
    plt.close()