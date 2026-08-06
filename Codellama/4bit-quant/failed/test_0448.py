import pytest
from src_0448 import task_func
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def test_task_func():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    n_components = 2
    random_state = None
    result = task_func(data, n_components, random_state)
    assert isinstance(result, dict)
    assert "transformed_data" in result
    assert "ax" in result
    assert isinstance(result["transformed_data"], np.ndarray)
    assert result["transformed_data"].shape[1] == n_components
    assert isinstance(result["ax"], plt.Axes)

def test_task_func_with_different_n_components():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    n_components = 3
    random_state = None
    result = task_func(data, n_components, random_state)
    assert isinstance(result, dict)
    assert "transformed_data" in result
    assert "ax" in result
    assert isinstance(result["transformed_data"], np.ndarray)
    assert result["transformed_data"].shape[1] == n_components
    assert isinstance(result["ax"], plt.Axes)

def test_task_func_with_random_state():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    n_components = 2
    random_state = 42
    result = task_func(data, n_components, random_state)
    assert isinstance(result, dict)
    assert "transformed_data" in result
    assert "ax" in result
    assert isinstance(result["transformed_data"], np.ndarray)
    assert result["transformed_data"].shape[1] == n_components
    assert isinstance(result["ax"], plt.Axes)

if __name__ == "__main__":
    pytest.main()