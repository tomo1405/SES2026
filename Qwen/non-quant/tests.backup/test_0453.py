import pytest
from src_0453 import task_func
import numpy as np

@pytest.mark.parametrize("n_samples, n_features, random_seed", [
    (100, 10, None),
    (50, 5, 42),
    (200, 20, 0),
])
def test_task_func(n_samples, n_features, random_seed):
    predictions, coefficients, intercept, mse = task_func(n_samples, n_features, random_seed)
    
    # Check that predictions is a numpy array with the correct shape
    assert isinstance(predictions, np.ndarray)
    assert predictions.shape[0] == int(n_samples * 0.2)
    
    # Check that coefficients is a numpy array with the correct shape
    assert isinstance(coefficients, np.ndarray)
    assert coefficients.shape == (n_features,)
    
    # Check that intercept is a float
    assert isinstance(intercept, float)
    
    # Check that mse is a float and non-negative
    assert isinstance(mse, float)
    assert mse >= 0

def test_task_func_default_parameters():
    predictions, coefficients, intercept, mse = task_func()
    
    # Check default parameters
    assert predictions.shape[0] == 20  # 20% of 100 samples
    assert coefficients.shape == (10,)
    assert isinstance(intercept, float)
    assert isinstance(mse, float)
    assert mse >= 0

def test_task_func_random_seed_consistency():
    _, _, _, mse1 = task_func(random_seed=42)
    _, _, _, mse2 = task_func(random_seed=42)
    
    # Check that the same random seed produces the same MSE
    assert mse1 == mse2