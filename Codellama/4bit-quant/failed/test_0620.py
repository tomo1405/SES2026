import pytest
from src_0620 import task_func

def test_task_func():
    # Test with default parameters
    results_df, model = task_func(10, 5)
    assert results_df.shape == (5, 3)
    assert model.coef_[0] > 0

    # Test with custom parameters
    results_df, model = task_func(10, 5, rng_seed=42)
    assert results_df.shape == (5, 3)
    assert model.coef_[0] > 0

    # Test with invalid parameters
    with pytest.raises(ValueError):
        task_func(0, 5)
    with pytest.raises(ValueError):
        task_func(10, 0)
    with pytest.raises(ValueError):
        task_func(-1, 5)
    with pytest.raises(ValueError):
        task_func(10, -1)