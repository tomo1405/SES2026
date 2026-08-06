import pytest
from src_0229 import task_func
import pandas as pd
import numpy as np

def test_task_func_input_not_dataframe():
    df = "not a dataframe"
    dct = {"column1": "value1", "column2": "value2"}
    with pytest.raises(ValueError):
        task_func(df, dct)

def test_task_func_input_dataframe_empty():
    df = pd.DataFrame()
    dct = {"column1": "value1", "column2": "value2"}
    with pytest.raises(ValueError):
        task_func(df, dct)

def test_task_func_input_dataframe_no_columns():
    df = pd.DataFrame([[1, 2, 3, 4, 5]])
    dct = {"column1": "value1", "column2": "value2"}
    with pytest.raises(ValueError):
        task_func(df, dct)

def test_task_func_input_dataframe_no_rows():
    df = pd.DataFrame(columns=COLUMNS)
    dct = {"column1": "value1", "column2": "value2"}
    with pytest.raises(ValueError):
        task_func(df, dct)

def test_task_func_input_dataframe_no_values():
    df = pd.DataFrame(columns=COLUMNS, index=range(5))
    dct = {"column1": "value1", "column2": "value2"}
    with pytest.raises(ValueError):
        task_func(df, dct)

def test_task_func_input_dataframe_valid():
    df = pd.DataFrame(columns=COLUMNS, index=range(5), data=np.random.rand(5, 5))
    dct = {"column1": "value1", "column2": "value2"}
    result = task_func(df, dct)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (5, 5)
    assert result.columns.tolist() == COLUMNS
    assert result.index.tolist() == COLUMNS
    assert np.allclose(result.values, np.corrcoef(df.values, rowvar=False))