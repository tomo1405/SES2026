import pytest
from src_0223 import task_func
import math
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Test with a simple list of angles in radians
    input_list = [math.radians(30), math.radians(45), math.radians(60)]
    cumsum, ax = task_func(input_list)
    
    # Check if the cumulative sum is correct
    expected_cumsum = np.cumsum(sorted(input_list, key=lambda x: (math.degrees(x), x)))
    assert np.array_equal(cumsum, expected_cumsum)
    
    # Check if the plot has the correct title and labels
    assert ax.get_title() == "Cumulative Sum Plot"
    assert ax.get_xlabel() == "Index"
    assert ax.get_ylabel() == "Cumulative Sum"

# To run the tests, use the following command in your terminal:
# pytest -v