import pytest
from src_0442 import task_func
import numpy as np

def test_task_func_input_types():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    
    with pytest.raises(TypeError):
        task_func(P.tolist(), T)

def test_task_func_computation():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    
    expected_result = np.array([[22, 26, 30], [50, 62, 74]])
    
    result, _ = task_func(P, T)
    
    assert np.array_equal(result, expected_result)

def test_task_func_visualization():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    
    _, ax = task_func(P, T)
    
    assert ax is not None
    assert ax.name == "3d"