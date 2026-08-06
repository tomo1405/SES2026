python
import numpy as np
import pytest
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
from src_0775 import task_func

def test_task_func():
    # Test default values
    assert task_func() == (0.0, RandomForestRegressor(n_estimators=100, random_state=None))

    # Test num_samples / cv < 2
    with pytest.raises(ValueError):
        task_func(num_samples=10, cv=5)

    # Test random_seed
    assert task_func(random_seed=42)[0] == task_func(random_seed=42)[0]

    # Test n_estimators
    assert task_func(n_estimators=50)[1].n_estimators == 50

    # Test cv
    assert len(task_func(cv=3)[1].cv_results_) == 3

    # Test num_samples
    assert len(task_func(num_samples=1000)[1].estimators_) == 1000