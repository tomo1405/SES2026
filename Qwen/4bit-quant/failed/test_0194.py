import pytest
from src_0194 import task_func
import pandas as pd

def test_task_func_returns_dataframe():
    df = task_func(5, 3)
    assert isinstance(df, pd.DataFrame)

def test_task_func_correct_number_of_rows():
    rows = 7
    df = task_func(rows, 2)
    assert len(df) == rows

def test_task_func_correct_number_of_columns():
    columns = 4
    df = task_func(3, columns)
    assert len(df.columns) == columns

def test_task_func_column_data_types():
    df = task_func(5, 7)
    for col in df.columns:
        data_type = df[col].apply(type).iloc[0]
        assert data_type in [str, int, float, list, tuple, dict, set]

def test_task_func_str_column_values():
    df = task_func(5, 1)
    for value in df['col0']:
        assert isinstance(value, str) and len(value) == 5

def test_task_func_int_float_column_values():
    df = task_func(5, 2)
    for col in ['col1', 'col2']:
        for value in df[col]:
            assert isinstance(value, (int, float))

def test_task_func_list_tuple_dict_set_column_values():
    df = task_func(5, 4)
    for col in ['col3', 'col4', 'col5', 'col6']:
        for value in df[col]:
            assert isinstance(value, (list, tuple, dict, set))

def test_task_func_randomness():
    df1 = task_func(5, 3)
    df2 = task_func(5, 3)
    assert not df1.equals(df2)