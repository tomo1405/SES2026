import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
from src_0775 import task_func
import pytest

def test_task_func_with_default_args():
    mean_cv_score, model = task_func()
    assert isinstance(mean_cv_score, float)
    assert isinstance(model, RandomForestRegressor)

def test_task_func_with_custom_args():
    mean_cv_score, model = task_func(num_samples=200, n_estimators=50, random_seed=42, cv=10)
    assert isinstance(mean_cv_score, float)
    assert isinstance(model, RandomForestRegressor)

def test_task_func_with_invalid_args():
    with pytest.raises(ValueError):
        task_func(num_samples=10, cv=2)