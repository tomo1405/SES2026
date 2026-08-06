import pytest
from src_0443 import task_func
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def test_task_func():
    P = np.random.rand(3, 3, 3)
    T = np.random.rand(3, 3, 3)
    tensor_shape = (3, 3, 3)

    result, ax = task_func(P, T, tensor_shape)

    assert isinstance(result, np.ndarray)
    assert result.shape == (3, 2)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "PCA Result Visualization"
    assert ax.get_xlabel() == "Principal Component 1"
    assert ax.get_ylabel() == "Principal Component 2"

def test_task_func_invalid_input():
    P = np.random.rand(3, 3, 3)
    T = np.random.rand(3, 3, 3)
    tensor_shape = (3, 3, 3)

    with pytest.raises(TypeError):
        task_func(P, T, tensor_shape)

    with pytest.raises(ValueError):
        task_func(P, T, tensor_shape)