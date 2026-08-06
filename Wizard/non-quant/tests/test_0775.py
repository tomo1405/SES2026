python
import numpy as np
import pytest
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor

def task_func(num_samples=100, n_estimators=100, random_seed=None, cv=5):
    
    if num_samples / cv < 2:
        raise ValueError("num_samples / cv should be greater than or equal to 2.")

    np.random.seed(random_seed)
    X = np.random.randn(num_samples, 5)
    y = np.sum(X, axis=1) + np.random.randn(num_samples)
    
    model = RandomForestRegressor(n_estimators=n_estimators,
                                  random_state=random_seed
                                  )
    
    cv_scores = cross_val_score(model, X, y, cv=cv)
    
    return np.mean(cv_scores), model

def test_task_func():
    # Test case 1: default values
    assert task_func() == (0.0, RandomForestRegressor(n_estimators=100, random_state=None))
    
    # Test case 2: custom values
    assert task_func(num_samples=10, n_estimators=50, random_seed=42, cv=3) == (0.0, RandomForestRegressor(n_estimators=50, random_state=42))
    
    # Test case 3: invalid values
    with pytest.raises(ValueError):
        task_func(num_samples=10, n_estimators=50, random_seed=42, cv=1)