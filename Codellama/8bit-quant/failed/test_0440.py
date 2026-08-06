import pytest
from src_0440 import task_func
import numpy as np
import seaborn as sns

def test_task_func_input_type():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[5, 6], [7, 8]])
    with pytest.raises(TypeError):
        task_func(P, T)

def test_task_func_output_type():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[5, 6], [7, 8]])
    result, heatmap = task_func(P, T)
    assert isinstance(result, np.ndarray)
    assert isinstance(heatmap, sns.heatmap)

def test_task_func_output_shape():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[5, 6], [7, 8]])
    result, heatmap = task_func(P, T)
    assert result.shape == (2, 2)
    assert heatmap.shape == (2, 2)

def test_task_func_output_values():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[5, 6], [7, 8]])
    result, heatmap = task_func(P, T)
    expected_result = np.array([[14, 32], [32, 77]])
    expected_heatmap = sns.heatmap(expected_result)
    np.testing.assert_array_equal(result, expected_result)
    assert heatmap.data == expected_heatmap.data