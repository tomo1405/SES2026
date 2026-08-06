import pytest
from src_0979 import task_func
import numpy as np
import pandas as pd

def test_task_func_input_validation():
    # Test with non-2D input
    with pytest.raises(ValueError, match="Input must be a 2D numpy array."):
        task_func([1, 2, 3])

    # Test with empty array
    assert task_func(np.array([])).equals(pd.DataFrame(columns=["PC1", "PC2"]))

    # Test with empty columns
    assert task_func(np.array([[1], [2], [3]])).equals(pd.DataFrame(columns=["PC1", "PC2"]))

def test_task_func_with_seed():
    array = np.array([[1, 2], [3, 4], [5, 6]])
    df1 = task_func(array, seed=42)
    df2 = task_func(array, seed=42)
    assert df1.equals(df2)

def test_task_func_without_seed():
    array = np.array([[1, 2], [3, 4], [5, 6]])
    df1 = task_func(array)
    df2 = task_func(array)
    assert not df1.equals(df2)

def test_task_func_pca_components():
    array = np.array([[1, 2], [3, 4], [5, 6]])
    df = task_func(array)
    assert list(df.columns) == ["PC1", "PC2"]

    array_single_feature = np.array([[1], [2], [3]])
    df_single_feature = task_func(array_single_feature)
    assert list(df_single_feature.columns) == ["PC1"]

def test_task_func_data_transformation():
    array = np.array([[1, 2], [3, 4], [5, 6]])
    df = task_func(array)
    assert df.shape == (array.shape[0], 2)