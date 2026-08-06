import pytest
from src_0696 import task_func
import numpy as np
from sklearn.decomposition import PCA

def test_task_func_with_valid_input():
    tuples_list = [(1, 2), (3, 4), (5, 6)]
    n_components = 1
    result = task_func(tuples_list, n_components)
    assert isinstance(result, np.ndarray)
    assert result.shape == (3, n_components)

def test_task_func_with_zero_components():
    tuples_list = [(1, 2), (3, 4), (5, 6)]
    n_components = 0
    with pytest.raises(ValueError) as excinfo:
        task_func(tuples_list, n_components)
    assert "n_components must be between 0 and min(n_samples, n_features)" in str(excinfo.value)

def test_task_func_with_more_components_than_features():
    tuples_list = [(1, 2), (3, 4), (5, 6)]
    n_components = 3
    with pytest.raises(ValueError) as excinfo:
        task_func(tuples_list, n_components)
    assert "n_components must be between 0 and min(n_samples, n_features)" in str(excinfo.value)

def test_task_func_with_single_sample():
    tuples_list = [(1, 2)]
    n_components = 1
    result = task_func(tuples_list, n_components)
    assert isinstance(result, np.ndarray)
    assert result.shape == (1, n_components)

def test_task_func_with_negative_components():
    tuples_list = [(1, 2), (3, 4), (5, 6)]
    n_components = -1
    with pytest.raises(ValueError) as excinfo:
        task_func(tuples_list, n_components)
    assert "n_components must be between 0 and min(n_samples, n_features)" in str(excinfo.value)

def test_task_func_with_non_numeric_data():
    tuples_list = [("a", "b"), ("c", "d"), ("e", "f")]
    n_components = 1
    with pytest.raises(ValueError) as excinfo:
        task_func(tuples_list, n_components)
    assert "Input data contains non-numeric values" in str(excinfo.value)