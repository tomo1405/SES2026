python
import numpy as np
import pytest
from src_0773 import task_func

def test_task_func():
    # Test case 1: default values
    assert task_func() == pytest.approx(0.0, abs=1e-6)

    # Test case 2: custom values
    assert task_func(num_samples=100, k=2, d=1, random_seed=42) == pytest.approx(0.0, abs=1e-6)

    # Test case 3: invalid values
    with pytest.raises(ValueError):
        task_func(num_samples=-100)
    with pytest.raises(ValueError):
        task_func(k=0)
    with pytest.raises(ValueError):
        task_func(d=-1)
    with pytest.raises(ValueError):
        task_func(random_seed='invalid')