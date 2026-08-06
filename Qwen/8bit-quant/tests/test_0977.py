import pytest
from src_0977 import task_func
import numpy as np
import pandas as pd

def test_task_func_input_validation():
    with pytest.raises(ValueError):
        task_func(np.array([1, 2, 3]))

def test_task_func_output_shape():
    records = np.array([[1, 2], [3, 4]])
    df = task_func(records)
    assert df.shape == (2, 2)

def test_task_func_columns_shuffle():
    records = np.array([[1, 2], [3, 4]])
    df1 = task_func(records, random_seed=0)
    df2 = task_func(records, random_seed=1)
    assert not df1.columns.equals(df2.columns)

def test_task_func_data_normalization():
    records = np.array([[1, 2], [3, 4]])
    df = task_func(records)
    assert np.allclose(df.mean(), 0, atol=1e-6)
    assert np.allclose(df.std(), 1, atol=1e-6)

def test_task_func_random_seed_consistency():
    records = np.array([[1, 2], [3, 4]])
    df1 = task_func(records, random_seed=0)
    df2 = task_func(records, random_seed=0)
    assert df1.equals(df2)

def test_task_func_default_random_seed():
    records = np.array([[1, 2], [3, 4]])
    df1 = task_func(records)
    df2 = task_func(records, random_seed=None)
    assert df1.equals(df2)