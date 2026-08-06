import pytest
from src_0978 import task_func
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def test_task_func():
    # Test case 1: input array is 2-dimensional and non-empty
    array = np.array([[1, 2, 3], [4, 5, 6]])
    features = ["a", "b", "c"]
    seed = 123
    ax = task_func(array, features, seed)
    assert ax.get_xlabel() == "a"
    assert ax.get_ylabel() == "b"
    assert ax.get_zlabel() == "c"

    # Test case 2: input array is not 2-dimensional
    array = np.array([1, 2, 3])
    with pytest.raises(ValueError):
        task_func(array, features, seed)

    # Test case 3: input array is empty
    array = np.array([[]])
    with pytest.raises(ValueError):
        task_func(array, features, seed)

    # Test case 4: features list does not match the number of columns in the array
    array = np.array([[1, 2, 3], [4, 5, 6]])
    features = ["a", "b"]
    with pytest.raises(ValueError):
        task_func(array, features, seed)

    # Test case 5: seed is not None
    array = np.array([[1, 2, 3], [4, 5, 6]])
    features = ["a", "b", "c"]
    seed = 123
    ax = task_func(array, features, seed)
    assert ax.get_xlabel() == "a"
    assert ax.get_ylabel() == "b"
    assert ax.get_zlabel() == "c"

    # Test case 6: seed is None
    array = np.array([[1, 2, 3], [4, 5, 6]])
    features = ["a", "b", "c"]
    seed = None
    ax = task_func(array, features, seed)
    assert ax.get_xlabel() == "a"
    assert ax.get_ylabel() == "b"
    assert ax.get_zlabel() == "c"