import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src_0977 import task_func
import pytest

records_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
records_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

def test_task_func_valid_input():
    df = task_func(records_2d)
    assert isinstance(df, pd.DataFrame)

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(records_3d)

def test_task_func_random_seed():
    df1 = task_func(records_2d, random_seed=0)
    df2 = task_func(records_2d, random_seed=0)
    assert df1.equals(df2)

def test_task_func_shuffle_features():
    df1 = task_func(records_2d)
    df2 = task_func(records_2d)
    assert not df1.columns.equals(df2.columns)

def test_task_func_scaler():
    df = task_func(records_2d)
    scaler = StandardScaler()
    scaled_records = scaler.fit_transform(records_2d)
    assert np.array_equal(df.values, scaled_records)