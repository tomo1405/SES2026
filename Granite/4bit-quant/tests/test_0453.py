import numpy as np
from src_0453 import task_func


def test_task_func():
    predictions, coefficients, intercept, mse = task_func()
    assert isinstance(predictions, np.ndarray), "predictions should be a numpy array"
    assert isinstance(coefficients, np.ndarray), "coefficients should be a numpy array"
    assert isinstance(intercept, float), "intercept should be a float"
    assert isinstance(mse, float), "mse should be a float"
    assert mse >= 0, "mse should be non-negative"