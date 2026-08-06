import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pytest
from src_0978 import task_func

@pytest.fixture
def array():
    return np.array([[1, 2, 3], [4, 5, 6]])

@pytest.fixture
def features():
    return ["A", "B", "C"]

def test_seed(array, features):
    seed = 42
    ax = task_func(array, features, seed)
    assert ax.get_xlabel() == "A"
    assert ax.get_ylabel() == "B"

def test_without_seed(array, features):
    ax = task_func(array, features)
    assert ax.get_xlabel() == "1"
    assert ax.get_ylabel() == "2"

def test_invalid_input_array(features):
    with pytest.raises(ValueError):
        task_func(np.array([]), features)
    with pytest.raises(ValueError):
        task_func(np.array([[]]), features)

def test_invalid_features(array):
    with pytest.raises(ValueError):
        task_func(array, ["A"])