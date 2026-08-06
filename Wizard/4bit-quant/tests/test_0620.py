python
import pytest
from src_0620 import task_func

def test_task_func():
    # Test with default rng_seed
    results_df, model = task_func(5, 2)
    assert len(results_df) == 5
    assert len(results_df.columns) == 3
    assert model.coef_[0] == pytest.approx(1000, abs=1)

    # Test with custom rng_seed
    results_df, model = task_func(5, 2, rng_seed=42)
    assert len(results_df) == 5
    assert len(results_df.columns) == 3
    assert model.coef_[0] == pytest.approx(1000, abs=1)

    # Test with invalid goals parameter
    with pytest.raises(ValueError):
        task_func(0, 2)

    # Test with invalid penalties parameter
    with pytest.raises(ValueError):
        task_func(5, 0)