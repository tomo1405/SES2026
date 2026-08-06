import pandas as pd
from src_0496 import task_func


def test_task_func_output_shape():
    days = 10
    df = task_func(days)
    assert df.shape == (days, 5), f"Expected shape ({days}, 5), but got {df.shape}"

def test_task_func_columns():
    days = 10
    df = task_func(days)
    expected_columns = ['Groceries', 'Entertainment', 'Rent', 'Utilities', 'Miscellaneous']
    assert list(df.columns) == expected_columns, f"Expected columns {expected_columns}, but got {list(df.columns)}"

def test_task_func_index():
    days = 10
    df = task_func(days)
    expected_index = pd.date_range(start="2023-01-01", periods=days, freq="D")
    assert df.index.equals(expected_index), f"Expected index {expected_index}, but got {df.index}"

def test_task_func_random_seed():
    days = 10
    df1 = task_func(days, random_seed=0)
    df2 = task_func(days, random_seed=0)
    assert df1.equals(df2), "Dataframes with the same random seed should be identical"

def test_task_func_random_values():
    days = 10
    df = task_func(days)
    assert df.values.min() >= 0 and df.values.max() <= 99, "Random values should be between 0 and 99"