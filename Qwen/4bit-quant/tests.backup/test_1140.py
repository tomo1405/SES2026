import pytest
from src_1140 import task_func
import numpy as np

@pytest.fixture
def sample_data():
    data = {
        'Hours': [1, 2, 3, 4, 5],
        'Scores': [20, 22, 29, 33, 38]
    }
    return data

def test_task_func(sample_data):
    mse = task_func(sample_data)
    assert isinstance(mse, float), "The result should be a float."
    assert mse >= 0, "Mean Squared Error cannot be negative."

def test_task_func_with_zero_variance(sample_data):
    zero_variance_data = {
        'Hours': [1, 1, 1, 1, 1],
        'Scores': [20, 22, 29, 33, 38]
    }
    mse = task_func(zero_variance_data)
    assert mse == 0, "Mean Squared Error should be zero when there's no variance in the input data."

def test_task_func_with_large_variance(sample_data):
    large_variance_data = {
        'Hours': [1, 2, 3, 4, 5],
        'Scores': [100, 200, 300, 400, 500]
    }
    mse = task_func(large_variance_data)
    assert mse > 0, "Mean Squared Error should be greater than zero with large variance in the input data."