import pytest
from src_0397 import task_func

def test_task_func():
    # Test case 1: sample_size is a positive integer
    ax = task_func(mu=0, sigma=1, sample_size=100)
    assert ax is not None

    # Test case 2: sample_size is not a positive integer
    with pytest.raises(ValueError):
        task_func(mu=0, sigma=1, sample_size=0)

    # Test case 3: sample_size is a negative integer
    with pytest.raises(ValueError):
        task_func(mu=0, sigma=1, sample_size=-10)