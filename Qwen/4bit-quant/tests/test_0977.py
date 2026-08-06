import pytest
from src_0977 import task_func
import numpy as np
import pandas as pd

def test_task_func_input_type():
    with pytest.raises(ValueError):
        task_func(np.array([1, 2, 3]))

def test_task_func_input_dimensions():
    with pytest.raises(ValueError):
        task_func(np.array([[1, 2], [3, 4]]).reshape(4))

def test_task_func_output_type():
    records = np.array([[1, 2], [3, 4]])
    result = task_func(records)
    assert isinstance(result, pd.DataFrame)

def test_task_func_output_shape():
    records = np.array([[1, 2], [3, 4]])
    result = task_func(records)
    assert result.shape == (2, 2)

def test_task_func_random_seed():
    records = np.array([[1, 2], [3, 4]])
    df1 = task_func(records, random_seed=0)
    df2 = task_func(records, random_seed=0)
    assert df1.equals(df2)

def test_task_func_column_names():
    records = np.array([[1, 2], [3, 4]])
    df = task_func(records)
    assert len(df.columns) == 2
    assert all(isinstance(col, str) for col in df.columns)

def test_task_func_column_values():
    records = np.array([[1, 2], [3, 4]])
    df = task_func(records)
    assert df.values.mean() == pytest.approx(0, abs=1e-6)
    assert df.values.std() == pytest.approx(1, abs=1e-6)