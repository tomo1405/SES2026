import pandas as pd
import pytest
from src_0224 import task_func


def test_task_func_input_df_not_df():
    df = "not a DataFrame"
    dct = {"a": "b"}
    with pytest.raises(ValueError):
        task_func(df, dct)

def test_task_func_input_dct_not_dict():
    df = pd.DataFrame({"a": [1, 2, 3]})
    dct = "not a dictionary"
    with pytest.raises(ValueError):
        task_func(df, dct)

def test_task_func_input_columns_not_list():
    df = pd.DataFrame({"a": [1, 2, 3]})
    dct = {"a": "b"}
    columns = "not a list"
    with pytest.raises(ValueError):
        task_func(df, dct, columns)

def test_task_func_input_columns_not_object():
    df = pd.DataFrame({"a": [1, 2, 3]})
    dct = {"a": "b"}
    columns = ["a", "b"]
    with pytest.raises(ValueError):
        task_func(df, dct, columns)

def test_task_func_input_df_empty():
    df = pd.DataFrame()
    dct = {"a": "b"}
    with pytest.raises(ValueError):
        task_func(df, dct)

def test_task_func_input_dct_empty():
    df = pd.DataFrame({"a": [1, 2, 3]})
    dct = {}
    with pytest.raises(ValueError):
        task_func(df, dct)

def test_task_func_input_df_and_dct_empty():
    df = pd.DataFrame()
    dct = {}
    with pytest.raises(ValueError):
        task_func(df, dct)

def test_task_func_input_df_and_dct_not_empty():
    df = pd.DataFrame({"a": [1, 2, 3]})
    dct = {"a": "b"}
    result = task_func(df, dct)
    assert isinstance(result, pd.DataFrame)
    assert result.equals(pd.DataFrame({"a": [1, 2, 3]}))

def test_task_func_input_df_and_dct_not_empty_with_columns():
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    dct = {"a": "b"}
    columns = ["a"]
    result = task_func(df, dct, columns)
    assert isinstance(result, pd.DataFrame)
    assert result.equals(pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}))

def test_task_func_input_df_and_dct_not_empty_with_columns_not_object():
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    dct = {"a": "b"}
    columns = ["a", "b"]
    with pytest.raises(ValueError):
        task_func(df, dct, columns)

def test_task_func_input_df_and_dct_not_empty_with_columns_not_in_df():
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    dct = {"a": "b"}
    columns = ["c"]
    with pytest.raises(ValueError):
        task_func(df, dct, columns)

def test_task_func_input_df_and_dct_not_empty_with_columns_not_in_dct():
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    dct = {"a": "b"}
    columns = ["a", "c"]
    with pytest.raises(ValueError):
        task_func(df, dct, columns)

def test_task_func_input_df_and_dct_not_empty_with_columns_not_in_df_and_dct():
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    dct = {"a": "b"}
    columns = ["c", "d"]
    with pytest.raises(ValueError):
        task_func(df, dct, columns)

def test_task_func_input_df_and_dct_not_empty_with_columns_not_object_and_not_in_df_and_dct():
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    dct = {"a": "b"}
    columns = ["c", "d", "e"]
    with pytest.raises(ValueError):
        task_func(df, dct, columns)