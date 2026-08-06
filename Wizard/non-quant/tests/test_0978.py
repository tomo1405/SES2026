python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pytest

def task_func(array, features=None, seed=None):

    if seed is not None:
        np.random.seed(seed)

    if array.size == 0 or len(array.shape) != 2:
        raise ValueError("Input array must be 2-dimensional and non-empty.")

    if features is not None and len(features) != array.shape[1]:
        raise ValueError("Features list must match the number of columns in the array.")

    shuffled_array = np.random.permutation(array.T).T

    fig, ax = plt.subplots()
    sns.heatmap(
        shuffled_array,
        xticklabels=features if features is not None else np.arange(array.shape[1]) + 1,
        ax=ax,
    )

    return ax

def test_task_func():
    # Test case 1: Test with valid input
    array = np.array([[1, 2, 3], [4, 5, 6]])
    features = ['a', 'b', 'c']
    seed = 42
    ax = task_func(array, features, seed)
    assert ax is not None

    # Test case 2: Test with empty array
    with pytest.raises(ValueError):
        task_func(np.array([]), None, None)

    # Test case 3: Test with non-2D array
    with pytest.raises(ValueError):
        task_func(np.array([1, 2, 3]), None, None)

    # Test case 4: Test with different number of features
    with pytest.raises(ValueError):
        task_func(np.array([[1, 2, 3], [4, 5, 6]]), ['a', 'b'], None)

    # Test case 5: Test with invalid seed
    with pytest.raises(ValueError):
        task_func(np.array([[1, 2, 3], [4, 5, 6]]), None, 'invalid')