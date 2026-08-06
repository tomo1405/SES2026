import pytest
from src_0453 import task_func
import numpy as np

@pytest.mark.parametrize("n_samples, n_features, random_seed", [
    (100, 10, None),
    (200, 5, 42),
    (50, 20, 0),
])
def test_task_func(n_samples, n_features, random_seed):
    predictions, coefficients, intercept, mse = task_func(n_samples, n_features, random_seed)
    
    # Check that predictions and coefficients are numpy arrays
    assert isinstance(predictions, np.ndarray)
    assert isinstance(coefficients, np.ndarray)
    assert isinstance(intercept, float)
    
    # Check that the number of predictions matches the test set size
    assert len(predictions) == int(n_samples * 0.2)
    
    # Check that the number of coefficients matches the number of features
    assert len(coefficients) == n_features
    
    # Check that MSE is a non-negative float
    assert isinstance(mse, float)
    assert mse >= 0.0

def test_task_func_default_parameters():
    predictions, coefficients, intercept, mse = task_func()
    
    # Check default values
    assert predictions.shape[0] == 20  # 20% of 100 samples
    assert coefficients.shape[0] == 10  # 10 features
    assert isinstance(intercept, float)
    assert isinstance(mse, float)
    assert mse >= 0.0

def test_task_func_random_seed():
    _, _, _, mse1 = task_func(random_seed=42)
    _, _, _, mse2 = task_func(random_seed=42)
    
    # Check that with the same random seed, MSEs are the same
    assert np.isclose(mse1, mse2)