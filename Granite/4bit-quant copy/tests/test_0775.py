import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
from src_0775 import task_func

def test_task_func():
    num_samples = 100
    n_estimators = 100
    random_seed = 42
    cv = 5
    
    try:
        mean_cv_score, model = task_func(num_samples, n_estimators, random_seed, cv)
        assert isinstance(mean_cv_score, float)
        assert isinstance(model, RandomForestRegressor)
    except ValueError:
        assert False, "ValueError should not be raised"
    
    num_samples = 10
    cv = 5
    try:
        mean_cv_score, model = task_func(num_samples, n_estimators, random_seed, cv)
        assert True
    except ValueError:
        assert False, "ValueError should be raised"