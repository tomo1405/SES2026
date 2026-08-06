import numpy as np
import pandas as pd
import pytest
from src_0979 import task_func


def test_task_func_with_valid_input():
    array = np.array([[1, 2, 3], [4, 5, 6]])
    expected_output = pd.DataFrame(data([[1.5, 2.5], [4.5, 5.5]], columns=["PC1", "PC2"]))
    output = task_func(array)
    assert output.equals(expected_output)

def test_task_func_with_invalid_input():
    array = np.array([1, 2, 3])
    with pytest.raises(ValueError) as exc_info:
        task_func(array)
    assert "Input must be a 2D numpy array." in str(exc_info.value)

def test_task_func_with_zero_columns():
    array = np.array([[]])
    expected_output = pd.DataFrame(columns=["PC1", "PC2"])
    output = task_func(array)
    assert output.equals(expected_output)

def test_task_func_with_zero_rows():
    array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    array = array[:0]
    expected_output = pd.DataFrame(columns=["PC1", "PC2"])
    output = task_func(array)
    assert output.equals(expected_output)

def test_task_func_with_seed():
    array = np.array([[1, 2, 3], [4, 5, 6]])
    seed = 42
    expected_output = pd.DataFrame(data([[4.5, 5.5], [1.5, 2.5]], columns=["PC1", "PC2"]))
    output = task_func(array, seed=seed)
    assert output.equals(expected_output)