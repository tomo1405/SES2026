import matplotlib.pyplot as plt
import numpy as np
import pytest
from src_0242 import task_func


@pytest.fixture
def sample_data():
    return [(1, 2), (3, 4), (5, 6)]

def test_task_func_with_non_empty_data(sample_data):
    original, normalized, ax = task_func(sample_data)
    
    # Check if the original array is correctly created
    expected_original = np.array([2, 4, 6])
    assert np.array_equal(original, expected_original)
    
    # Check if the normalized array is correctly created
    expected_normalized = preprocessing.normalize([expected_original])[0]
    assert np.allclose(normalized, expected_normalized)
    
    # Check if the plot is correctly created
    assert isinstance(ax, plt.Axes)

def test_task_func_with_empty_data():
    original, normalized, ax = task_func([])
    
    # Check if the original array is correctly created
    expected_original = np.array([])
    assert np.array_equal(original, expected_original)
    
    # Check if the normalized array is correctly created
    expected_normalized = np.array([])
    assert np.array_equal(normalized, expected_normalized)
    
    # Check if the plot is correctly created
    assert isinstance(ax, plt.Axes)

def test_task_func_with_single_element_data():
    original, normalized, ax = task_func([(1, 1)])
    
    # Check if the original array is correctly created
    expected_original = np.array([1])
    assert np.array_equal(original, expected_original)
    
    # Check if the normalized array is correctly created
    expected_normalized = np.array([1])  # Normalizing a single element array results in the same array
    assert np.array_equal(normalized, expected_normalized)
    
    # Check if the plot is correctly created
    assert isinstance(ax, plt.Axes)