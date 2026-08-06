import pytest
from src_0946 import task_func

def test_task_func():
    # Test that the function returns the correct type
    assert isinstance(task_func(), np.ndarray)

    # Test that the function returns the correct shape
    assert task_func().shape == (13,)

    # Test that the function returns the correct values
    expected_values = np.array([100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700])
    assert np.allclose(task_func(), expected_values)