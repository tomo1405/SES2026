import pytest
from src_0452 import task_func

def test_task_func():
    X_transformed, ax = task_func(n_components=2, N_SAMPLES=500, N_FEATURES=50, random_seed=42)
    assert X_transformed.shape == (500, 2)
    assert ax is not None
    with pytest.raises(ValueError):
        task_func(n_components=1, N_SAMPLES=500, N_FEATURES=50, random_seed=42)