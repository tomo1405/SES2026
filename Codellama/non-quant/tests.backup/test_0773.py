import pytest
from src_0773 import task_func

def test_task_func():
    # Test with default values
    mse = task_func()
    assert mse > 0

    # Test with custom values
    mse = task_func(num_samples=100, k=2, d=1)
    assert mse > 0

    # Test with random seed
    mse = task_func(random_seed=42)
    assert mse > 0