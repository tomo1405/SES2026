import pytest
from src_0951 import task_func

def test_task_func():
    # Test with default parameters
    U, s, Vh = task_func()
    assert isinstance(U, np.ndarray), "U should be a numpy array"
    assert isinstance(s, np.ndarray), "s should be a numpy array"
    assert isinstance(Vh, np.ndarray), "Vh should be a numpy array"
    assert U.shape == (3, 3), "U should have the shape (3, 3)"
    assert s.shape == (min(3, 2), "s should have the shape (min(3, 2),)"
    assert Vh.shape == (2, 2), "Vh should have the shape (2, 2)"

    # Additional tests can be added to check the numerical properties if needed