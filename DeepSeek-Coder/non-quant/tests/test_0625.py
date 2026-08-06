import pytest
from src_0625 import task_func
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def test_task_func():
    # Create a sample input
    data = np.array([[1, 2], [3, 4], [5, 6]])
    
    # Call the function
    result, _ = task_func(data)
    
    # Assertions
    assert result.shape == (3, 2)
    assert np.allclose(result, np.array([[-2.82842712, -0.70710678],
                                          [-0.70710678,  0.70710678],
                                          [ 0.70710678,  0.70710678]]))

    # Check if the plot is created without errors
    plt.close()