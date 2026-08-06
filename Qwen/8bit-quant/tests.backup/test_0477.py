import pytest
from src_0477 import task_func
import numpy as np

@pytest.fixture
def sample_data():
    X = np.array([1, 2, 3, 4, 5])
    Y = np.array([2, 4, 6, 8, 10])
    return X, Y

def test_task_func(sample_data):
    X, Y = sample_data
    params, ax = task_func(X, Y)
    
    # Check if the parameters are returned as a list
    assert isinstance(params, list)
    assert len(params) == 3
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 2  # One for scatter and one for fit line
    assert len(ax.collections) == 1  # One for scatter plot

    # Check if the function returns the correct number of parameters
    a, b, c = params
    assert isinstance(a, float)
    assert isinstance(b, float)
    assert isinstance(c, float)

    # Check if the function fits the data correctly
    fitted_Y = a * X**2 + b * X + c
    assert np.allclose(fitted_Y, Y, atol=1e-6)