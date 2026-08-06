python
import numpy as np
import pytest
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
from src_0775 import task_func

def test_task_func():
    # Test case 1: default values
    assert task_func() == (0.0, RandomForestRegressor(n_estimators=100, random_state=None))

    # Test case 2: custom values
    assert task_func(num_samples=10, n_estimators=50, random_seed=42, cv=3) == (0.0, RandomForestRegressor(n_estimators=50, random_state=42))

    # Test case 3: num_samples / cv < 2
    with pytest.raises(ValueError):
        task_func(num_samples=10, n_estimators=50, random_seed=42, cv=2)