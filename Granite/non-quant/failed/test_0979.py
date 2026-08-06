import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from src_0979 import task_func
import pytest

def test_task_func_with_valid_input():
    array = np.array([[1, 2, 3], [4, 5, 6]])
    expected_output = pd.DataFrame(data([[1.5, 3.5], [4.5, 6.5]], columns=["PC1", "PC2"]))
    output = task_func(array)
    assert output.equals(expected_output)

def test_task_func_with_invalid_input():
    with pytest.raises(ValueError) as excinfo:
        task_func("invalid input")
    assert "Input must be a 2D numpy array." in str(excinfo.value)

def test_task_func_with_zero_size_input():
    array = np.array([])
    expected_output = pd.DataFrame(columns=["PC1", "PC2"])
    output = task_func(array)
    assert output.equals(expected_output)

def test_task_func_with_one_dimensional_input():
    array = np.array([1, 2, 3])
    with pytest.raises(ValueError) as excinfo:
        task_func(array)
    assert "Input must be a 2D numpy array." in str(excinfo.value)

def test_task_func_with_seed():
    array = np.array([[1, 2, 3], [4, 5, 6]])
    seed = 42
    expected_output = pd.DataFrame(data([[1.5, 3.5], [4.5, 6.5]], columns=["PC1", "PC2"]))
    output = task_func(array, seed=seed)
    assert output.equals(expected_output)