import numpy as np
import pytest
from src_0453 import task_func


def test_task_func():
    # Test with default parameters
    predictions, coefficients, intercept, mse = task_func()
    assert isinstance(predictions, np.ndarray)
    assert isinstance(coefficients, np.ndarray)
    assert isinstance(intercept, float)
    assert isinstance(mse, float)

    # Test with custom parameters
    predictions, coefficients, intercept, mse = task_func(n_samples=1000, n_features=5, random_seed=42)
    assert isinstance(predictions, np.ndarray)
    assert isinstance(coefficients, np.ndarray)
    assert isinstance(intercept, float)
    assert isinstance(mse, float)

    # Test with invalid parameters
    with pytest.raises(ValueError):
        task_func(n_samples=-1, n_features=10, random_seed=42)
    with pytest.raises(ValueError):
        task_func(n_samples=100, n_features=-1, random_seed=42)
    with pytest.raises(ValueError):
        task_func(n_samples=100, n_features=10, random_seed="invalid")