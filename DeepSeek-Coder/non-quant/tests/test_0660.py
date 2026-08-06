import pytest
from src_0660 import task_func
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def test_task_func():
    # Create test data
    x = np.array([1, 2, 3])
    y = np.array([[1, 2, 3], [4, 5, 6]])
    labels = ["Label1", "Label2"]

    # Call the function
    fig = task_func(x, y, labels)

    # Add assertions to check the output
    assert fig is not None
    assert plt.get_fignums() > 0

    # Clean up
    plt.close()