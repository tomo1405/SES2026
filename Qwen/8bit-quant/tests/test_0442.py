import matplotlib.pyplot as plt
import numpy as np
import pytest
from src_0442 import task_func


def test_task_func_input_types():
    P = np.array([[1, 2], [3, 4]])
    T = np.random.rand(2, 3, 4)
    
    with pytest.raises(TypeError):
        task_func(P.tolist(), T)
    
    with pytest.raises(TypeError):
        task_func(P, T.tolist())

def test_task_func_result_shape():
    P = np.array([[1, 2], [3, 4]])
    T = np.random.rand(2, 3, 4)
    result, ax = task_func(P, T)
    
    assert result.shape == (2, 4), f"Expected shape (2, 4), but got {result.shape}"

def test_task_func_visualization():
    P = np.array([[1, 2], [3, 4]])
    T = np.random.rand(2, 3, 4)
    result, ax = task_func(P, T)
    
    assert isinstance(ax, plt.Axes), "Expected ax to be an instance of plt.Axes"
    assert ax.name == '3d', "Expected ax to be a 3D subplot"

def test_task_func_with_zeros():
    P = np.zeros((2, 2))
    T = np.random.rand(2, 3, 4)
    result, ax = task_func(P, T)
    
    assert np.allclose(result, np.zeros((2, 4))), "Expected result to be all zeros"

def test_task_func_with_identity():
    P = np.eye(2)
    T = np.random.rand(2, 3, 4)
    result, ax = task_func(P, T)
    
    assert np.allclose(result, T.sum(axis=1)), "Expected result to be the sum of T along axis 1"