import pytest
from src_0775 import task_func

def test_task_func():
    # Test that the function raises an error when num_samples / cv is less than 2
    with pytest.raises(ValueError):
        task_func(num_samples=10, cv=5)

    # Test that the function returns the correct mean and model
    mean, model = task_func(num_samples=100, n_estimators=100, random_seed=42, cv=5)
    assert mean > 0
    assert isinstance(model, RandomForestRegressor)