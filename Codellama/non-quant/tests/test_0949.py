import numpy as np
from src_0949 import task_func


def test_task_func():
    # Test that the function returns a numpy array
    assert isinstance(task_func(), np.ndarray)

    # Test that the function returns a matrix with the correct shape
    assert task_func().shape == (3, 2)

    # Test that the function returns a matrix with values between 0 and 1
    assert np.all(task_func() >= 0) and np.all(task_func() <= 1)

    # Test that the function returns a matrix with the same values as the input matrix
    matrix = np.random.rand(3, 2)
    assert np.all(task_func(matrix) == matrix)

    # Test that the function returns a matrix with the same values as the input matrix, but scaled
    matrix = np.random.rand(3, 2)
    scaled_matrix = task_func(matrix)
    assert np.all(scaled_matrix >= 0) and np.all(scaled_matrix <= 1)
    assert np.all(scaled_matrix != matrix)