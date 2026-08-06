import pytest
from src_0773 import task_func

def test_task_func():
    # Test that the function returns a float
    assert isinstance(task_func(), float)

    # Test that the function returns the correct value for a specific input
    assert task_func(num_samples=1000, k=5, d=2, random_seed=None) == 0.0

    # Test that the function raises a ValueError if the input is invalid
    with pytest.raises(ValueError):
        task_func(num_samples=-1, k=5, d=2, random_seed=None)

    with pytest.raises(ValueError):
        task_func(num_samples=1000, k=-1, d=2, random_seed=None)

    with pytest.raises(ValueError):
        task_func(num_samples=1000, k=5, d=-1, random_seed=None)