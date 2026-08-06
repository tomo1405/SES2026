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

def test_task_func_input_dataframe_valid():
    df = pd.DataFrame(np.random.randint(0, 100, size=(10, 5)), columns=COLUMNS)
    dct = {"column1": "value1", "column2": "value2"}
    result = task_func(df, dct)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (5, 5)
    assert result.columns.tolist() == COLUMNS
    assert result.index.tolist() == COLUMNS

def test_task_func_input_dataframe_valid_no_replacement():
    df = pd.DataFrame(np.random.randint(0, 100, size=(10, 5)), columns=COLUMNS)
    dct = {}
    result = task_func(df, dct)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (5, 5)
    assert result.columns.tolist() == COLUMNS
    assert result.index.tolist() == COLUMNS

def test_task_func_input_dataframe_valid_replacement():
    df = pd.DataFrame(np.random.randint(0, 100, size=(10, 5)), columns=COLUMNS)
    dct = {"column1": "value1", "column2": "value2"}
    result = task_func(df, dct)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (5, 5)
    assert result.columns.tolist() == COLUMNS
    assert result.index.tolist() == COLUMNS
    assert result.iloc[0, 0] == "value1"
    assert result.iloc[0, 1] == "value2"