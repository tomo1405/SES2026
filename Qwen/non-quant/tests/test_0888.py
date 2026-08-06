import pandas as pd
from src_0888 import task_func


def test_task_func_output_type():
    T1 = [['1', '2'], ['3']]
    df = task_func(T1)
    assert isinstance(df, pd.DataFrame)

def test_task_func_column_names():
    T1 = [['1', '2'], ['3']]
    df = task_func(T1)
    expected_columns = ['Col_1', 'Col_2', 'Col_3']
    assert list(df.columns) == expected_columns

def test_task_func_row_count():
    T1 = [['1', '2'], ['3']]
    row_num = 50
    df = task_func(T1, row_num=row_num)
    assert len(df) == row_num

def test_task_func_random_seed():
    T1 = [['1', '2'], ['3']]
    seed = 42
    df1 = task_func(T1, seed=seed)
    df2 = task_func(T1, seed=seed)
    assert df1.equals(df2)

def test_task_func_no_seed():
    T1 = [['1', '2'], ['3']]
    df1 = task_func(T1)
    df2 = task_func(T1)
    assert not df1.equals(df2)

def test_task_func_empty_input():
    T1 = []
    df = task_func(T1)
    assert df.empty

def test_task_func_single_element():
    T1 = [['1']]
    df = task_func(T1)
    assert len(df.columns) == 1