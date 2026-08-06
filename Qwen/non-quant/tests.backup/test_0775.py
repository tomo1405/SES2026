import pytest
from src_0775 import task_func

def test_task_func_default_parameters():
    mean_score, model = task_func()
    assert isinstance(mean_score, float)
    assert isinstance(model, RandomForestRegressor)

def test_task_func_custom_parameters():
    mean_score, model = task_func(num_samples=200, n_estimators=200, random_seed=42, cv=10)
    assert isinstance(mean_score, float)
    assert isinstance(model, RandomForestRegressor)

def test_task_func_invalid_num_samples_cv_ratio():
    with pytest.raises(ValueError):
        task_func(num_samples=5, cv=3)

def test_task_func_random_seed_reproducibility():
    mean_score1, _ = task_func(random_seed=42)
    mean_score2, _ = task_func(random_seed=42)
    assert mean_score1 == mean_score2

def test_task_func_different_random_seeds():
    mean_score1, _ = task_func(random_seed=42)
    mean_score2, _ = task_func(random_seed=123)
    assert mean_score1 != mean_score2

def test_task_func_cv_greater_than_num_samples():
    with pytest.raises(ValueError):
        task_func(num_samples=5, cv=10)