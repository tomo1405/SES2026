import pytest
from src_0194 import task_func
import pandas as pd
import numpy as np

def test_task_func_return_type():
    df = task_func(5, 3)
    assert isinstance(df, pd.DataFrame)

def test_task_func_column_count():
    df = task_func(5, 3)
    assert len(df.columns) == 3

def test_task_func_row_count():
    df = task_func(5, 3)
    assert len(df) == 5

def test_task_func_data_types():
    df = task_func(5, 3)
    for col in df.columns:
        data_type = df[col].apply(type).unique()
        assert len(data_type) == 1, f"Column {col} has mixed data types"

def test_task_func_data_type_contents():
    df = task_func(5, 3)
    for col in df.columns:
        data_type = df[col].apply(type).iloc[0]
        assert data_type in [str, int, float, list, tuple, dict, set], f"Column {col} has invalid data type {data_type}"

def test_task_func_str_column():
    df = task_func(5, 3)
    for col in df.columns:
        if df[col].apply(type).iloc[0] == str:
            assert all(isinstance(x, str) and len(x) == 5 for x in df[col]), f"Column {col} does not contain valid strings"

def test_task_func_int_float_columns():
    df = task_func(5, 3)
    for col in df.columns:
        if df[col].apply(type).iloc[0] in [int, float]:
            assert all(isinstance(x, (int, float)) and 0 <= x < 10 for x in df[col]), f"Column {col} does not contain valid integers/floats"

def test_task_func_list_tuple_dict_set_columns():
    df = task_func(5, 3)
    for col in df.columns:
        data_type = df[col].apply(type).iloc[0]
        if data_type in [list, tuple, dict, set]:
            for item in df[col]:
                assert isinstance(item, data_type), f"Column {col} contains invalid item type {type(item)}"
                if data_type == list:
                    assert all(isinstance(x, int) for x in item), f"Column {col} contains non-integer items"
                elif data_type == tuple:
                    assert all(isinstance(x, int) for x in item), f"Column {col} contains non-integer items"
                elif data_type == dict:
                    assert all(isinstance(k, int) and isinstance(v, int) for k, v in item.items()), f"Column {col} contains non-integer keys/values"
                elif data_type == set:
                    assert all(isinstance(x, int) for x in item), f"Column {col} contains non-integer items"