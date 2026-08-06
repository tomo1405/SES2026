import pytest
from src_0442 import task_func
import numpy as np
import matplotlib.pyplot as plt

# Test cases for the function
def test_task_func():
    # Test with valid inputs
    P = np.array([[1, 2, 3], [4, 5, 6]])
    T = np.array([[7, 8, 9], [10, 11, 12]])
    result, _ = task_func(P, T)
    assert isinstance(result, np.ndarray), "The result should be a numpy array"
    assert result.shape == (2, 3), "The shape of the result should be (2, 3)"

    # Add more test cases as needed

# Run the tests
if __name__ == "__main__":
    pytest.main()