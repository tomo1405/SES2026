import pandas as pd
from src_0380 import task_func


def test_task_func_length():
    length = 10
    df = task_func(length)
    assert len(df) == length

def test_task_func_columns():
    df = task_func(5)
    assert list(df.columns) == COLUMNS

def test_task_func_data_type():
    df = task_func(7)
    assert isinstance(df, pd.DataFrame)

def test_task_func_data_range():
    df = task_func(3)
    assert df.values.min() >= 0 and df.values.max() <= 99

def test_task_func_empty_df():
    df = task_func(0)
    assert df.empty