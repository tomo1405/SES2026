import pytest
from src_0223 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Test with a simple list of angles in radians
    input_list = [np.pi/4, np.pi/2, 3*np.pi/4, np.pi]
    expected_cumsum = [np.pi/4, 3*np.pi/4, 6*np.pi/4, 7*np.pi/4]
    
    cumsum, ax = task_func(input_list)
    
    # Check if the cumulative sum is correct
    np.testing.assert_allclose(cumsum, expected_cumsum)
    
    # Check if the plot title and labels are set correctly
    assert ax.get_title() == "Cumulative Sum Plot"
    assert ax.get_xlabel() == "Index"
    assert ax.get_ylabel() == "Cumulative Sum"

# Run the tests
if __name__ == "__main__":
    pytest.main()