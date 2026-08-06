import pytest
from src_0790 import task_func

def test_task_func():
    # Test that the function returns a numpy array
    assert isinstance(task_func(), np.ndarray)

    # Test that the function returns an array with the correct shape
    assert task_func().shape == (ARRAY_LENGTH, 1)

    # Test that the function returns an array with the correct values
    expected_array = np.array([[0.0], [0.25], [0.5], [0.75], [1.0]])
    assert np.allclose(task_func(), expected_array)