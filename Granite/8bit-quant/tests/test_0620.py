import pytest
from src_0620 import task_func


def test_task_func():
    goals = 5
    penalties = 3
    rng_seed = 42
    results_df, model = task_func(goals, penalties, rng_seed)
    assert len(results_df) == len(TEAMS)
    assert model.coef_[0] == -PENALTY_COST
    with pytest.raises(ValueError):
        task_func(goals, penalties, rng_seed='not_an_int')