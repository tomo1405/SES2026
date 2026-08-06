import pytest
from src_0443 import task_func
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def test_task_func():
    P = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    T = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    tensor_shape = (3, 3, 3)

    result, ax = task_func(P, T, tensor_shape)

    assert isinstance(result, np.ndarray)
    assert result.shape == (3, 2)
    assert isinstance(ax, plt.Axes)

def test_task_func_invalid_input():
    P = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    T = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    tensor_shape = (3, 3, 3)

    with pytest.raises(TypeError):
        task_func(P, T, tensor_shape)

    with pytest.raises(ValueError):
        task_func(P, T, tensor_shape)