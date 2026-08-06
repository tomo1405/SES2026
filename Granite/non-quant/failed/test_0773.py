import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from src_0773 import task_func
import pytest

def test_task_func_default_args():
    """
    Test the task_func function with default arguments.
    """
    mse = task_func()
    assert isinstance(mse, float)

def test_task_func_custom_args():
    """
    Test the task_func function with custom arguments.
    """
    num_samples = 100
    k = 2
    d = 1
    random_seed = 42
    mse = task_func(num_samples, k, d, random_seed)
    assert isinstance(mse, float)

def test_task_func_invalid_input():
    """
    Test the task_func function with invalid input.
    """
    with pytest.raises(ValueError):
        task_func('invalid', 'input')