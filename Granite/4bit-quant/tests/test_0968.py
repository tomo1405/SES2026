import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
from src_0968 import task_func
import pytest

def test_task_func():
    # Test case 1: Test with a simple sine function
    def sine(x):
        return np.sin(x)

    ax = task_func(sine)
    assert ax is not None
    # Add more assertions to test the output of the function

    # Test case 2: Test with a more complex function
    def complex_func(x):
        return x**2 + np.sin(x)

    ax = task_func(complex_func)
    assert ax is not None
    # Add more assertions to test the output of the function

if __name__ == "__main__":
    pytest.main()