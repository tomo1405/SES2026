import pytest
from src_0977 import task_func
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func_input_type():
    records = np.array([[1, 2, 3], [4, 5, 6]])
    random_seed = 0
    with pytest.raises(ValueError):
        task_func(records, random_seed)

def test_task_func_input_shape():
    records = np.array([[1, 2, 3], [4, 5, 6]])
    random_seed = 0
    with pytest.raises(ValueError):
        task_func(records, random_seed)

def test_task_func_output_type():
    records = np.array([[1, 2, 3], [4, 5, 6]])
    random_seed = 0
    df = task_func(records, random_seed)
    assert isinstance(df, pd.DataFrame)

def test_task_func_output_shape():
    records = np.array([[1, 2, 3], [4, 5, 6]])
    random_seed = 0
    df = task_func(records, random_seed)
    assert df.shape == (2, 3)

def test_task_func_output_values():
    records = np.array([[1, 2, 3], [4, 5, 6]])
    random_seed = 0
    df = task_func(records, random_seed)
    assert df.iloc[0, 0] == 1
    assert df.iloc[0, 1] == 2
    assert df.iloc[0, 2] == 3
    assert df.iloc[1, 0] == 4
    assert df.iloc[1, 1] == 5
    assert df.iloc[1, 2] == 6

def test_task_func_random_seed():
    records = np.array([[1, 2, 3], [4, 5, 6]])
    random_seed = 0
    df1 = task_func(records, random_seed)
    df2 = task_func(records, random_seed)
    assert df1.equals(df2)

    random_seed = 1
    df3 = task_func(records, random_seed)
    assert not df1.equals(df3)