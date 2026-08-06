import pytest
from src_0223 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Test with a simple list of angles in radians
    input_list = [math.pi/4, math.pi/2, 3*math.pi/4]
    cumsum, ax = task_func(input_list)
    
    # Check if the cumulative sum is calculated correctly
    expected_cumsum = np.cumsum(sorted(input_list, key=lambda x: (math.degrees(x), x)))
    assert np.allclose(cumsum, expected_cumsum), "The cumulative sum does not match the expected result."
    
    # Check if the plot is created with the correct title and labels
    assert ax.get_title() == "Cumulative Sum Plot", "The plot title is incorrect."
    assert ax.get_xlabel() == "Index", "The x-axis label is incorrect."
    assert ax.get_ylabel() == "Cumulative Sum", "The y-axis label is incorrect."

# Run the tests
if __name__ == "__main__":
    pytest.main()