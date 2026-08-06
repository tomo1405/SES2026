import pytest
from src_0453 import task_func

def test_task_func():
    # Test that the function returns the correct number of outputs
    predictions, coefficients, intercept, mse = task_func()
    assert len(predictions) == 100
    assert len(coefficients) == 10
    assert intercept is not None
    assert mse is not None

    # Test that the function returns the correct types of outputs
    assert isinstance(predictions, np.ndarray)
    assert isinstance(coefficients, np.ndarray)
    assert isinstance(intercept, float)
    assert isinstance(mse, float)

    # Test that the function returns the correct values for the outputs
    assert np.allclose(predictions, np.array([0.5, 0.5, 0.5, 0.5, 0.5]))
    assert np.allclose(coefficients, np.array([0.5, 0.5, 0.5, 0.5, 0.5]))
    assert intercept == 0.5
    assert mse == 0.5