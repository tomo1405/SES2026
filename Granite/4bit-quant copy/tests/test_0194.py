import pandas as pd
import numpy as np
from random import choice
from src_0194 import task_func

DATA_TYPES = [str, int, float, list, tuple, dict, set]

def test_task_func():
    rows = 10
    columns = 5
    df = task_func(rows, columns)
    assert isinstance(df, pd.DataFrame)
    assert len(df.columns) == columns
    for col in df.columns:
        assert len(df[col]) == rows

def test_task_func_data_types():
    rows = 10
    columns = 5
    df = task_func(rows, columns)
    for col in df.columns:
        assert df[col].dtype in DATA_TYPES

def test_task_func_str_data_type():
    rows = 10
    columns = 5
    df = task_func(rows, columns)
    for col in df.columns:
        if df[col].dtype == str:
            for value in df[col]:
                assert isinstance(value, str)
                assert len(value) == 5

def test_task_func_int_or_float_data_type():
    rows = 10
    columns = 5
    df = task_func(rows, columns)
    for col in df.columns:
        if df[col].dtype in [int, float]:
            for value in df[col]:
                assert isinstance(value, df[col].dtype)
                assert 0 <= value <= 9

def test_task_func_list_data_type():
    rows = 10
    columns = 5
    df = task_func(rows, columns)
    for col in df.columns:
        if df[col].dtype == list:
            for value in df[col]:
                assert isinstance(value, list)
                assert 1 <= len(value) <= 5
                assert all(isinstance(item, int) for item in value)
                assert all(0 <= item <= 9 for item in value)

def test_task_func_tuple_data_type():
    rows = 10
    columns = 5
    df = task_func(rows, columns)
    for col in df.columns:
        if df[col].dtype == tuple:
            for value in df[col]:
                assert isinstance(value, tuple)
                assert 1 <= len(value) <= 5
                assert all(isinstance(item, int) for item in value)
                assert all(0 <= item <= 9 for item in value)

def test_task_func_dict_data_type():
    rows = 10
    columns = 5
    df = task_func(rows, columns)
    for col in df.columns:
        if df[col].dtype == dict:
            for value in df[col]:
                assert isinstance(value, dict)
                assert 1 <= len(value) <= 5
                assert all(isinstance(key, int) for key in value.keys())
                assert all(isinstance(value, int) for value in value.values())
                assert all(0 <= key <= 9 for key in value.keys())
                assert all(0 <= value <= 9 for value in value.values())

def test_task_func_set_data_type():
    rows = 10
    columns = 5
    df = task_func(rows, columns)
    for col in df.columns:
        if df[col].dtype == set:
            for value in df[col]:
                assert isinstance(value, set)
                assert 1 <= len(value) <= 5
                assert all(isinstance(item, int) for item in value)
                assert all(0 <= item <= 9 for item in value)