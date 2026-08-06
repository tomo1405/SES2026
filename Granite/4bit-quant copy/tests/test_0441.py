import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src_0441 import task_func

def test_task_func():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[1, 2], [3, 4], [5, 6]])
    expected_result = np.array([[1.5, 3.5], [2.5, 4.5]])

    result = task_func(P, T)

    assert np.array_equal(result, expected_result)

def test_task_func_empty_inputs():
    P = np.array([])
    T = np.array([])

    with pytest.raises(ValueError) as excinfo:
        task_func(P, T)
    assert "Inputs cannot be empty." in str(excinfo.value)

def test_task_func_incompatible_shapes():
    P = np.array([[1, 2], [3, 4]])
    T = np.array([[1, 2], [3, 4]])

    with pytest.raises(ValueError) as excinfo:
        task_func(P, T)
    assert "Matrix P shape 2 and Tensor T shape 2 are incompatible for tensor multiplication." in str(excinfo.value)