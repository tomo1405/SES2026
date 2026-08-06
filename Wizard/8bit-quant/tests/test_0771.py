python
import numpy as np
import pytest
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from src_0771 import task_func

def test_task_func():
    # Test case 1: default values
    r_squared, model = task_func()
    assert r_squared >= 0 and r_squared <= 1

    # Test case 2: custom values
    r_squared, model = task_func(num_samples=1000, noise_strength=0.5, random_seed=42, test_size=0.3)
    assert r_squared >= 0 and r_squared <= 1

    # Test case 3: invalid values
    with pytest.raises(ValueError):
        r_squared, model = task_func(num_samples=1000, noise_strength=0.5, random_seed=42, test_size=0.1)