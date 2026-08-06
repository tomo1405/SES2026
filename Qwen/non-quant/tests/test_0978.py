import matplotlib.pyplot as plt
import numpy as np
import pytest
from src_0978 import task_func


@pytest.fixture
def sample_array():
    return np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

@pytest.fixture
def features():
    return ['A', 'B', 'C']

def test_task_func_basic(sample_array):
    ax = task_func(sample_array)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_features(sample_array, features):
    ax = task_func(sample_array, features=features)
    assert isinstance(ax, plt.Axes)

def test_task_func_empty_array():
    with pytest.raises(ValueError):
        task_func(np.array([]))

def test_task_func_non_2d_array():
    with pytest.raises(ValueError):
        task_func(np.array([1, 2, 3]))

def test_task_func_mismatched_features(sample_array):
    with pytest.raises(ValueError):
        task_func(sample_array, features=['A', 'B'])

def test_task_func_with_seed(sample_array):
    ax1 = task_func(sample_array, seed=42)
    ax2 = task_func(sample_array, seed=42)
    assert np.array_equal(ax1.collections[0].get_offsets(), ax2.collections[0].get_offsets())

def test_task_func_without_features(sample_array):
    ax = task_func(sample_array)
    assert isinstance(ax, plt.Axes)