import pytest
from src_0978 import task_func
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def test_task_func_basic():
    # Test basic functionality
    array = np.array([[1, 2, 3], [4, 5, 6]])
    features = ['A', 'B', 'C']
    result = task_func(array, features=features)
    assert result is not None

def test_task_func_with_seed():
    # Test with seed
    array = np.array([[1, 2, 3], [4, 5, 6]])
    features = ['A', 'B', 'C']
    result = task_func(array, features=features, seed=42)
    assert result is not None

def test_task_func_invalid_input():
    # Test with invalid input
    array = np.array([[]])
    with pytest.raises(ValueError):
        task_func(array)

def test_task_func_no_features():
    # Test without features
    array = np.array([[1, 2, 3], [4, 5, 6]])
    result = task_func(array)
    assert result is not None

def test_task_func_invalid_features():
    # Test with invalid features
    array = np.array([[1, 2, 3], [4, 5, 6]])
    features = ['A']
    with pytest.raises(ValueError):
        task_func(array, features=features)