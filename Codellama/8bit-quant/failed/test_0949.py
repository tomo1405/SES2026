import pytest
from src_0949 import task_func

def test_task_func():
    # Test that the function returns a numpy array
    assert isinstance(task_func(), np.ndarray)

    # Test that the function returns a matrix with the correct shape
    assert task_func().shape == (3, 2)

    # Test that the function returns a matrix with values between 0 and 1
    assert np.all(task_func() >= 0) and np.all(task_func() <= 1)

    # Test that the function returns a matrix with the same values as the input matrix
    # when the seed is set to 42
    assert np.all(task_func(seed=42) == np.random.rand(3, 2))