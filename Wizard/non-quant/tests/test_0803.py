python
import numpy as np
import itertools
import pytest

def task_func(dimension, seed=42):
    np.random.seed(seed)  # Ensure reproducible results
    
    if dimension <= 0:
        raise ValueError("The dimension must be a positive integer")
    
    matrix = np.random.randint(1, 101, size=(dimension, dimension))
    flat_list = matrix.flatten().tolist()
    
    combinations = list(itertools.combinations(flat_list, 2))
    
    return matrix, flat_list

def test_task_func():
    # Test case 1: Valid input
    matrix, flat_list = task_func(5, seed=42)
    assert matrix.shape == (5, 5)
    assert len(flat_list) == 25
    assert len(combinations) == 10
    
    # Test case 2: Invalid input (dimension <= 0)
    with pytest.raises(ValueError):
        task_func(0, seed=42)
    
    # Test case 3: Invalid input (dimension not an integer)
    with pytest.raises(TypeError):
        task_func(3.5, seed=42)