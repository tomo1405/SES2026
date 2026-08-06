import pytest
from src_1065 import task_func
import numpy as np
import seaborn as sns

def test_task_func():
    # Test with a sample 2D array
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    result = task_func(arr)
    assert result is not None, "The function should return a valid heatmap object"

    # Add more assertions to check the expected behavior of the function
    # For example, you can check if the title is set correctly, etc.