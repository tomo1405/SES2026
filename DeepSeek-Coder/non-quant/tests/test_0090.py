import pytest
from src_0090 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.preprocessing import StandardScaler

@pytest.fixture
def sample_data():
    data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
    return data

def test_task_func(sample_data):
    data = sample_data
    result = task_func(data, 1, 2)
    assert len(result[1]) == 4  # Check if the number of outliers removed is correct
    assert np.array_equal(result[0], data)  # Check if the original data is not modified

def test_plot(sample_data):
    data = sample_data
    result = task_func(data, 1, 2)
    assert plt.get_fignums() == 1  # Check if the plot is created