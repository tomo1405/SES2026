import pytest
from src_0443 import task_func
import numpy as np

def test_task_func_type_error():
    P = [1, 2, 3]
    T = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    with pytest.raises(TypeError):
        task_func(P, T)

def test_task_func_shape_error():
    P = np.array([1, 2, 3])
    T = np.array([[1, 2], [3, 4]])
    with pytest.raises(ValueError):
        task_func(P, T)

def test_task_func_correct_output_shape():
    P = np.array([1, 2, 3])
    T = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    pca_result, ax = task_func(P, T)
    assert pca_result.shape == (3, 2)

def test_task_func_pca_result():
    P = np.array([1, 2, 3])
    T = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    pca_result, ax = task_func(P, T)
    expected_mean = np.mean(pca_result, axis=0)
    assert np.allclose(expected_mean, np.zeros(2))

def test_task_func_ax_type():
    P = np.array([1, 2, 3])
    T = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    _, ax = task_func(P, T)
    assert isinstance(ax, plt.Axes)