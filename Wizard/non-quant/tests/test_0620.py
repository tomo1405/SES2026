python
import pytest
from src_0620 import task_func

def test_task_func():
    # Test case 1
    goals = 5
    penalties = 2
    rng_seed = 42
    results_df, model = task_func(goals, penalties, rng_seed)
    assert results_df.shape == (5, 3)
    assert model.coef_[0] == pytest.approx(1000.0)
    assert model.intercept_ == pytest.approx(0.0)

    # Test case 2
    goals = 10
    penalties = 5
    rng_seed = 123
    results_df, model = task_func(goals, penalties, rng_seed)
    assert results_df.shape == (5, 3)
    assert model.coef_[0] == pytest.approx(1000.0)
    assert model.intercept_ == pytest.approx(0.0)

    # Test case 3
    goals = 15
    penalties = 10
    rng_seed = None
    results_df, model = task_func(goals, penalties, rng_seed)
    assert results_df.shape == (5, 3)
    assert model.coef_[0] == pytest.approx(1000.0)
    assert model.intercept_ == pytest.approx(0.0)