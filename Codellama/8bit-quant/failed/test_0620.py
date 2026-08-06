import pytest
from src_0620 import task_func

def test_task_func():
    # Test with default values
    results_df, model = task_func(goals=10, penalties=5)
    assert results_df.shape == (5, 3)
    assert model.coef_[0] > 0

    # Test with custom values
    results_df, model = task_func(goals=20, penalties=10, rng_seed=42)
    assert results_df.shape == (5, 3)
    assert model.coef_[0] > 0

    # Test with invalid values
    with pytest.raises(ValueError):
        task_func(goals=-1, penalties=5)
    with pytest.raises(ValueError):
        task_func(goals=10, penalties=-1)
    with pytest.raises(ValueError):
        task_func(goals=10, penalties=5, rng_seed=-1)