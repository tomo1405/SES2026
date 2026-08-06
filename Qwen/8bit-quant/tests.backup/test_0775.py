import pytest
from src_0775 import task_func

def test_task_func_basic():
    mean_score, model = task_func()
    assert isinstance(mean_score, float)
    assert isinstance(model, RandomForestRegressor)

def test_task_func_with_custom_params():
    mean_score, model = task_func(num_samples=200, n_estimators=50, random_seed=42, cv=10)
    assert isinstance(mean_score, float)
    assert isinstance(model, RandomForestRegressor)

def test_task_func_invalid_num_samples_cv_ratio():
    with pytest.raises(ValueError):
        task_func(num_samples=5, cv=3)

def test_task_func_random_seed_reproducibility():
    _, model1 = task_func(random_seed=42)
    _, model2 = task_func(random_seed=42)
    assert str(model1) == str(model2)

def test_task_func_cv_greater_than_one():
    with pytest.raises(ValueError):
        task_func(num_samples=10, cv=1)