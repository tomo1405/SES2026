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
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'Features'
    assert ax.get_ylabel() == 'Samples'
    assert ax.get_title() == 'Shuffled array'
    assert ax.get_xticklabels() == ['a', 'b', 'c']
    assert ax.get_yticklabels() == ['1', '2']
    assert ax.collections[0].get_array().tolist() == [[3, 2, 1], [6, 5, 4]]

    # Test case 2: Test with empty array
    with pytest.raises(ValueError):
        task_func(np.array([]))

    # Test case 3: Test with non-2D array
    with pytest.raises(ValueError):
        task_func(np.array([1, 2, 3]))

    # Test case 4: Test with different number of features
    with pytest.raises(ValueError):
        task_func(np.array([[1, 2, 3], [4, 5, 6]]), ['a', 'b'])

    # Test case 5: Test with invalid seed
    with pytest.raises(ValueError):
        task_func(np.array([[1, 2, 3], [4, 5, 6]]), seed='invalid')