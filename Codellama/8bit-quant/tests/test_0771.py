import numpy as np
import pytest
from src_0771 import task_func


def test_task_func_num_samples_too_small():
    with pytest.raises(ValueError):
        task_func(num_samples=1, noise_strength=1, random_seed=None, test_size=0.2)

def test_task_func_test_size_too_small():
    with pytest.raises(ValueError):
        task_func(num_samples=500, noise_strength=1, random_seed=None, test_size=0.01)

def test_task_func_random_seed_set():
    np.random.seed(42)
    r_squared, model = task_func(num_samples=500, noise_strength=1, random_seed=42, test_size=0.2)
    assert r_squared > 0.9
    assert model.coef_[0] == 2

def test_task_func_random_seed_not_set():
    r_squared, model = task_func(num_samples=500, noise_strength=1, random_seed=None, test_size=0.2)
    assert r_squared > 0.9
    assert model.coef_[0] == 2