import pytest
from src_0977 import task_func
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func():
    records = np.array([[1, 2, 3], [4, 5, 6]])
    random_seed = 0
    df = task_func(records, random_seed)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 3)
    assert np.allclose(df.values, np.array([[1, 2, 3], [4, 5, 6]]))

def test_task_func_random_seed():
    records = np.array([[1, 2, 3], [4, 5, 6]])
    random_seed = 1
    df = task_func(records, random_seed)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 3)
    assert np.allclose(df.values, np.array([[1, 2, 3], [4, 5, 6]]))

def test_task_func_invalid_input():
    records = np.array([[1, 2, 3], [4, 5, 6]])
    random_seed = 0
    with pytest.raises(ValueError):
        task_func(records, random_seed)

def test_task_func_invalid_input_type():
    records = "invalid"
    random_seed = 0
    with pytest.raises(TypeError):
        task_func(records, random_seed)

def test_task_func_invalid_input_shape():
    records = np.array([[1, 2, 3], [4, 5, 6]])
    random_seed = 0
    with pytest.raises(ValueError):
        task_func(records, random_seed)