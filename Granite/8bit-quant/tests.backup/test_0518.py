import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from src_0518 import task_func
import pytest

def test_task_func():
    array = [[1, 2], [3, 4], [5, 6]]
    df, transformed_data = task_func(array)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(transformed_data, np.ndarray)
    assert df.shape == (3, 2)
    assert transformed_data.shape == (3, 2)

def test_task_func_with_random_seed():
    array = [[1, 2], [3, 4], [5, 6]]
    df1, transformed_data1 = task_func(array, random_seed=42)
    df2, transformed_data2 = task_func(array, random_seed=42)
    assert np.array_equal(df1, df2)
    assert np.array_equal(transformed_data1, transformed_data2)

def test_task_func_with_default_random_seed():
    array = [[1, 2], [3, 4], [5, 6]]
    df1, transformed_data1 = task_func(array)
    df2, transformed_data2 = task_func(array)
    assert not np.array_equal(df1, df2)
    assert not np.array_equal(transformed_data1, transformed_data2)