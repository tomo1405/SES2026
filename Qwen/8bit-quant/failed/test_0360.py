import pytest
from src_0360 import task_func
import numpy as np

@pytest.fixture
def sample_data():
    return {
        'data1': np.array([1, 2, 3, 4, 5]),
        'data2': np.array([2, 4, 6, 8, 10])
    }

def test_task_func(sample_data):
    data_keys = ['data1', 'data2']
    correlation, ax = task_func(sample_data, data_keys)
    
    # Check if the correlation is 1.0 (perfect positive correlation)
    assert np.isclose(correlation, 1.0), "Correlation should be 1.0 for perfectly correlated data"
    
    # Check if the scatter plot has the correct number of points
    lines = ax.get_lines()
    assert len(lines) == 1, "There should be exactly one line in the scatter plot"
    xdata, ydata = lines[0].get_data()
    assert len(xdata) == 5 and len(ydata) == 5, "The scatter plot should have 5 data points"

def test_task_func_with_unrelated_data(sample_data):
    unrelated_data = {
        'data1': np.array([1, 2, 3, 4, 5]),
        'data2': np.array([5, 3, 1, 4, 2])
    }
    data_keys = ['data1', 'data2']
    correlation, ax = task_func(unrelated_data, data_keys)
    
    # Check if the correlation is close to 0.0 (no correlation)
    assert np.isclose(correlation, 0.0), "Correlation should be close to 0.0 for unrelated data"
    
    # Check if the scatter plot has the correct number of points
    lines = ax.get_lines()
    assert len(lines) == 1, "There should be exactly one line in the scatter plot"
    xdata, ydata = lines[0].get_data()
    assert len(xdata) == 5 and len(ydata) == 5, "The scatter plot should have 5 data points"