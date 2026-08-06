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

def test_task_func_invalid_cv():
    with pytest.raises(ValueError):
        task_func(num_samples=10, cv=5)

def test_task_func_random_seed_reproducibility():
    _, model1 = task_func(num_samples=100, random_seed=42)
    _, model2 = task_func(num_samples=100, random_seed=42)
    assert model1.get_params() == model2.get_params()

def test_task_func_cv_greater_than_num_samples():
    with pytest.raises(ValueError):
        task_func(num_samples=5, cv=6)