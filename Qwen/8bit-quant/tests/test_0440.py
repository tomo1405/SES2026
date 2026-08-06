import pytest
from src_0440 import task_func
import numpy as np
import seaborn as sns

def test_task_func_with_valid_input():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[5, 6], [7, 8]])
    result, heatmap = task_func(P, T)
    assert isinstance(result, np.ndarray)
    assert result.shape == (2, 2)
    assert isinstance(heatmap, sns.axisgrid.HeatMap)

def test_task_func_with_invalid_input_type():
    P = [1, 2]
    T = np.array([[5, 6], [7, 8]])
    with pytest.raises(TypeError):
        task_func(P, T)

def test_task_func_with_mismatched_dimensions():
    P = np.array([[1, 2, 3], [4, 5, 6]])
    T = np.array([[5, 6], [7, 8]])
    with pytest.raises(ValueError):
        task_func(P, T)

def test_task_func_with_zero_arrays():
    P = np.zeros((2, 3))
    T = np.zeros((3, 2))
    result, heatmap = task_func(P, T)
    assert np.allclose(result, np.zeros((2, 2)))

def test_task_func_with_identity_matrices():
    P = np.eye(2)
    T = np.eye(2)
    result, heatmap = task_func(P, T)
    expected_result = np.array([[1, 1], [1, 1]])
    assert np.allclose(result, expected_result)