import pandas as pd
from src_1071 import task_func


def test_task_func_empty_input():
    result = task_func([])
    assert result == [], "Expected an empty list for empty input"

def test_task_func_single_list():
    input_data = [['X', 'Y']]
    result = task_func(input_data)
    assert len(result) == 1, "Expected one DataFrame for one list"
    df = result[0]
    assert isinstance(df, pd.DataFrame), "Expected a DataFrame"
    assert list(df.columns) == ['X', 'Y'], "Expected columns 'X' and 'Y'"
    assert all(len(df[col]) == len(POSSIBLE_VALUES) for col in df.columns), "Expected each column to have the same number of rows as POSSIBLE_VALUES"

def test_task_func_multiple_lists():
    input_data = [['X', 'Y'], ['A', 'B', 'C']]
    result = task_func(input_data)
    assert len(result) == 2, "Expected two DataFrames for two lists"
    df1, df2 = result
    assert isinstance(df1, pd.DataFrame) and isinstance(df2, pd.DataFrame), "Expected DataFrames"
    assert list(df1.columns) == ['X', 'Y'] and list(df2.columns) == ['A', 'B', 'C'], "Expected correct columns for each DataFrame"
    assert all(len(df[col]) == len(POSSIBLE_VALUES) for df in [df1, df2] for col in df.columns), "Expected each column to have the same number of rows as POSSIBLE_VALUES"

def test_task_func_unique_values_per_column():
    input_data = [['X', 'Y']]
    result = task_func(input_data)
    df = result[0]
    for col in df.columns:
        assert len(set(df[col])) == len(POSSIBLE_VALUES), "Expected unique values in each column"

def test_task_func_shuffle():
    input_data = [['X', 'Y']]
    result = task_func(input_data)
    df = result[0]
    original_values = POSSIBLE_VALUES.copy()
    for col in df.columns:
        shuffled_values = list(df[col])
        shuffle(original_values)
        assert shuffled_values != original_values, "Expected shuffled values in each column"