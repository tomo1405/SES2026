import pytest
from src_0620 import task_func

def test_task_func():
    goals = 5
    penalties = 3
    rng_seed = 42
    results_df, model = task_func(goals, penalties, rng_seed)
    assert results_df.shape == (5, 3)
    assert model.coef_ == pytest.approx(1000)

def test_task_func_default_args():
    goals = 2
    penalties = 1
    results_df, model = task_func(goals, penalties)
    assert results_df.shape == (5, 3)
    assert model.coef_ == pytest.approx(1000)

def test_task_func_invalid_args():
    with pytest.raises(ValueError):
        task_func(-1, 2)
    with pytest.raises(ValueError):
        task_func(2, -1)