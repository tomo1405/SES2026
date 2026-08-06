import pytest
from src_0453 import task_func

def test_task_func():
    # Test with default parameters
    predictions, coefficients, intercept, mse = task_func()
    assert isinstance(predictions, np.ndarray), "Predictions should be a numpy array"
    assert isinstance(coefficients, np.ndarray), "Coefficients should be a numpy array"
    assert isinstance(intercept, (int, float)), "Intercept should be a number"
    assert isinstance(mse, (int, float)), "MSE should be a number"
    assert len(predictions) == len(X_test), "Predictions length should match the test set size"

    # Add more assertions as needed to cover different scenarios