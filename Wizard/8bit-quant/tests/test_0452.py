python
import numpy as np
import pytest
from src_0452 import task_func

def test_task_func():
    # Test case 1: n_components=2, N_SAMPLES=500, N_FEATURES=50, random_seed=None
    X_transformed, ax = task_func(n_components=2, N_SAMPLES=500, N_FEATURES=50, random_seed=None)
    assert X_transformed.shape == (500, 2)
    assert ax is not None
    
    # Test case 2: n_components=1, N_SAMPLES=500, N_FEATURES=50, random_seed=None
    X_transformed, ax = task_func(n_components=1, N_SAMPLES=500, N_FEATURES=50, random_seed=None)
    assert X_transformed.shape == (500, 1)
    assert ax is None
    
    # Test case 3: n_components=2, N_SAMPLES=100, N_FEATURES=10, random_seed=42
    X_transformed, ax = task_func(n_components=2, N_SAMPLES=100, N_FEATURES=10, random_seed=42)
    assert X_transformed.shape == (100, 2)
    assert ax is not None
    
    # Test case 4: n_components=1, N_SAMPLES=100, N_FEATURES=10, random_seed=42
    X_transformed, ax = task_func(n_components=1, N_SAMPLES=100, N_FEATURES=10, random_seed=42)
    assert X_transformed.shape == (100, 1)
    assert ax is None
    
    # Test case 5: n_components=2, N_SAMPLES=100, N_FEATURES=10, random_seed=None
    X_transformed, ax = task_func(n_components=2, N_SAMPLES=100, N_FEATURES=10, random_seed=None)
    assert X_transformed.shape == (100, 2)
    assert ax is not None
    
    # Test case 6: n_components=1, N_SAMPLES=100, N_FEATURES=10, random_seed=None
    X_transformed, ax = task_func(n_components=1, N_SAMPLES=100, N_FEATURES=10, random_seed=None)
    assert X_transformed.shape == (100, 1)
    assert ax is None