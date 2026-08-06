import pytest
from src_0775 import task_func

def test_task_func():
    # Test case 1: num_samples / cv < 2
    with pytest.raises(ValueError):
        task_func(num_samples=10, cv=5)

    # Test case 2: num_samples / cv >= 2
    mean, model = task_func(num_samples=100, cv=5)
    assert isinstance(mean, float)
    assert isinstance(model, RandomForestRegressor)

    # Test case 3: n_estimators < 1
    with pytest.raises(ValueError):
        task_func(num_samples=100, n_estimators=0, cv=5)

    # Test case 4: n_estimators >= 1
    mean, model = task_func(num_samples=100, n_estimators=10, cv=5)
    assert isinstance(mean, float)
    assert isinstance(model, RandomForestRegressor)

    # Test case 5: random_seed is not None
    mean, model = task_func(num_samples=100, n_estimators=10, random_seed=42, cv=5)
    assert isinstance(mean, float)
    assert isinstance(model, RandomForestRegressor)