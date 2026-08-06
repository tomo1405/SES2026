import numpy as np
from src_0453 import task_func


def test_task_func():
    predictions, coefficients, intercept, mse = task_func()
    assert isinstance(predictions, np.ndarray)
    assert isinstance(coefficients, np.ndarray)
    assert isinstance(intercept, float)
    assert isinstance(mse, float)