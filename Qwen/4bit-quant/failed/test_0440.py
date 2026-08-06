import pytest
from src_0440 import task_func
import numpy as np

def test_task_func_input_types():
    with pytest.raises(TypeError):
        task_func([1, 2, 3], np.array([1, 2, 3]))

    with pytest.raises(TypeError):
        task_func(np.array([1, 2, 3]), [1, 2, 3])

def test_task_func_result_shape():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[5, 6], [7, 8]])
    result, _ = task_func(P, T)
    assert result.shape == (2, 2), f"Expected result shape to be (2, 2), got {result.shape}"

def test_task_func_result_values():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[5, 6], [7, 8]])
    result, _ = task_func(P, T)
    expected_result = np.array([[59, 70], [139, 160]])
    assert np.array_equal(result, expected_result), f"Expected result to be {expected_result}, got {result}"

def test_task_func_heatmap_return_type():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[5, 6], [7, 8]])
    _, heatmap = task_func(P, T)
    assert isinstance(heatmap, sns.axisgrid.FacetGrid), "Expected heatmap to be an instance of sns.axisgrid.FacetGrid"

def test_task_func_with_empty_arrays():
    P = np.array([])
    T = np.array([])
    with pytest.raises(ValueError):
        task_func(P, T)

def test_task_func_with_mismatched_dimensions():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([1, 2, 3])
    with pytest.raises(ValueError):
        task_func(P, T)