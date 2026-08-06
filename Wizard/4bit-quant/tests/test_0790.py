python
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pytest

# Constants
ARRAY_LENGTH = 10

def task_func():
    np.random.seed(42)  # For reproducibility, as shown in your example
    array = np.random.randint(0, 10, ARRAY_LENGTH).reshape(-1, 1)
    scaler = MinMaxScaler()
    scaled_array = scaler.fit_transform(array)
    return scaled_array

def test_task_func():
    # Test if the function returns a numpy array
    assert isinstance(task_func(), np.ndarray)
    
    # Test if the function returns a scaled array
    assert (task_func() >= 0).all() and (task_func() <= 1).all()