import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
from src_0775 import task_func
import pytest

def test_task_func_with_valid_input():
    num_samples = 100
    n_estimators = 100
    random_seed = 42
    cv = 5
    
    mean_cv_score, model = task_func(num_samples, n_estimators, random_seed, cv)
    
    assert isinstance(mean_cv_score, float)
    assert isinstance(model, RandomForestRegressor)

def test_task_func_with_invalid_input():
    num_samples = 10
    n_estimators = 100
    random_seed = 42
    cv = 5
    
    with pytest.raises(ValueError):
        task_func(num_samples, n_estimators, random_seed, cv)