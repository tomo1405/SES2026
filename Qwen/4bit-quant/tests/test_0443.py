import pytest
from src_0443 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_input_types():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    with pytest.raises(TypeError):
        task_func(P.tolist(), T)

def test_task_func_tensor_shape():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    with pytest.raises(ValueError):
        task_func(P, T, tensor_shape=(2, 2))

def test_task_func_output_shape():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    pca_result, ax = task_func(P, T)
    assert pca_result.shape == (2, 2)

def test_task_func_plot():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    pca_result, ax = task_func(P, T)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_random_data():
    P = np.random.rand(4, 5)
    T = np.random.rand(5, 6, 7)
    pca_result, ax = task_func(P, T, tensor_shape=(5, 6, 7))
    assert pca_result.shape == (4, 2)
    assert isinstance(ax, plt.Axes)