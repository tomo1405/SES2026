import pytest
from src_0442 import task_func
import numpy as np

def test_task_func_input_types():
    with pytest.raises(TypeError):
        task_func([1, 2], np.array([[1, 2], [3, 4]]))
    with pytest.raises(TypeError):
        task_func(np.array([[1, 2], [3, 4]]), [1, 2])

def test_task_func_shapes():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    result, ax = task_func(P, T)
    assert result.shape == (P.shape[0], T.shape[2])

def test_task_func_result_values():
    P = np.array([[1, 0], [0, 1]])
    T = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    expected_result = np.array([[1, 2, 3], [10, 11, 12]])
    result, ax = task_func(P, T)
    assert np.array_equal(result, expected_result)

def test_task_func_visualization():
    P = np.array([[1, 0], [0, 1]])
    T = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    result, ax = task_func(P, T)
    assert isinstance(ax, plt.Axes)