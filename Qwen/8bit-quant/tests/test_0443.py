import pytest
from src_0443 import task_func
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def test_task_func_input_types():
    P = np.array([[1, 2], [3, 4]])
    T = np.random.rand(3, 3, 3)
    with pytest.raises(TypeError):
        task_func(P.tolist(), T)

def test_task_func_tensor_shape():
    P = np.array([[1, 2], [3, 4]])
    T = np.random.rand(4, 3, 3)
    with pytest.raises(ValueError):
        task_func(P, T)

def test_task_func_output_shape():
    P = np.array([[1, 2], [3, 4]])
    T = np.random.rand(3, 3, 3)
    pca_result, ax = task_func(P, T)
    assert pca_result.shape == (2, 2)

def test_task_func_pca_result():
    P = np.array([[1, 2], [3, 4]])
    T = np.random.rand(3, 3, 3)
    pca_result, ax = task_func(P, T)
    assert isinstance(pca_result, np.ndarray)
    assert isinstance(ax, plt.Axes)

def test_task_func_plot():
    P = np.array([[1, 2], [3, 4]])
    T = np.random.rand(3, 3, 3)
    _, ax = task_func(P, T)
    assert ax.get_title() == "PCA Result Visualization"
    assert ax.get_xlabel() == "Principal Component 1"
    assert ax.get_ylabel() == "Principal Component 2"