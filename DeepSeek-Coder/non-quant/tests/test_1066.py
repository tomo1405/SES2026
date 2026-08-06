import pytest
from src_1066 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Create a sample array for testing
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    
    # Call the function
    result = task_func(arr)
    
    # Add assertions to verify the output
    assert result is not None, "The function did not return a value"
    assert isinstance(result, plt.Axes), "The function did not return a valid plot"

    # Close the plot to avoid hanging the tests
    plt.close()