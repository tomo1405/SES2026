import pandas as pd
import pytest
from src_0224 import task_func


def test_task_func_input_not_df():
    df = "not a DataFrame"
    dct = {"a": "b"}
    columns = None
    with pytest.raises(ValueError):
        task_func(df, dct, columns)

def test_task_func_input_df_not_object():
    df = pd.DataFrame({"a": [1, 2, 3]})
    dct = {"a": "b"}
    columns = None
    with pytest.raises(ValueError):
        task_func(df, dct, columns)

def test_task_func_input_dct_not_dict():
    df = pd.DataFrame({"a": ["a", "b", "c"]})
    dct = "not a dictionary"
    columns = None
    with pytest.raises(ValueError):
        task_func(df, dct, columns)

def test_task_func_input_columns_not_list():
    df = pd.DataFrame({"a": ["a", "b", "c"]})
    dct = {"a": "b"}
    columns = "not a list"
    with pytest.raises(ValueError):
        task_func(df, dct, columns)

def test_task_func_input_columns_not_in_df():
    df = pd.DataFrame({"a": ["a", "b", "c"]})
    dct = {"a": "b"}
    columns = ["d"]
    with pytest.raises(ValueError):
        task_func(df, dct, columns)

def test_task_func_input_columns_not_object():
    df = pd.DataFrame({"a": ["a", "b", "c"]})
    dct = {"a": "b"}
    columns = ["a"]
    with pytest.raises(ValueError):
        task_func(df, dct, columns)

def test_task_func_output_not_df():
    df = pd.DataFrame({"a": ["a", "b", "c"]})
    dct = {"a": "b"}
    columns = None
    output = task_func(df, dct, columns)
    assert isinstance(output, pd.DataFrame)

def test_task_func_output_columns_not_encoded():
    df = pd.DataFrame({"a": ["a", "b", "c"]})
    dct = {"a": "b"}
    columns = None
    output = task_func(df, dct, columns)
    assert all(output.columns == df.columns)

def test_task_func_output_columns_encoded():
    df = pd.DataFrame({"a": ["a", "b", "c"]})
    dct = {"a": "b"}
    columns = ["a"]
    output = task_func(df, dct, columns)
    assert all(output.columns == df.columns)
    assert all(output["a"] == [0, 1, 2])

def test_task_func_output_columns_not_standardized():
    df = pd.DataFrame({"a": [1, 2, 3]})
    dct = {"a": "b"}
    columns = None
    output = task_func(df, dct, columns)
    assert all(output.columns == df.columns)

def test_task_func_output_columns_standardized():
    df = pd.DataFrame({"a": [1, 2, 3]})
    dct = {"a": "b"}
    columns = None
    output = task_func(df, dct, columns)
    assert all(output.columns == df.columns)
    assert all(output["a"] == [0, 1, 2])