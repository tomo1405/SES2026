import pytest
from src_0453 import task_func

def test_task_func():
    predictions, coefficients, intercept, mse = task_func()
    assert isinstance(predictions, np.ndarray)
    assert isinstance(coefficients, np.ndarray)
    assert isinstance(intercept, float)
    assert isinstance(mse, float)
    assert predictions.shape[0] == coefficients.shape[0] == X_test.shape[0]
    assert coefficients.shape[1] == X_train.shape[1]