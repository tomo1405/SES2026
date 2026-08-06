import pytest
from src_0277 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def test_task_func():
    # Test with a sample matrix
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    skewness, kurtosis, _ = task_func(matrix)
    
    assert isinstance(skewness, float), "Skewness should be a float"
    assert isinstance(kurtosis, float), "Kurtosis should be a float"
    assert isinstance(_, plt.Axes), "The plot should be generated"

    # Additional assertions can be added to check the plot or other outputs if necessary