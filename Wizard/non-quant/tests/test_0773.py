python
import numpy as np
import pytest
from src_0773 import task_func

def test_task_func():
    # Test case 1: default values
    assert task_func() == 0.0

    # Test case 2: custom values
    assert task_func(num_samples=10, k=2, d=1, random_seed=42) == 0.0

    # Test case 3: invalid values
    with pytest.raises(ValueError):
        task_func(num_samples=-10)
    with pytest.raises(ValueError):
        task_func(k=-2)
    with pytest.raises(ValueError):
        task_func(d=-1)
    with pytest.raises(ValueError):
        task_func(random_seed='invalid')