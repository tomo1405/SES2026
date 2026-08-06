import pytest
from src_0172 import task_func
import pandas as pd
import collections

# Constants
VEGETABLES = ['Carrot', 'Potato', 'Tomato', 'Cabbage', 'Spinach']

def test_task_func_with_default_seed():
    vegetable_dict = {'A': 'Carrot', 'B': 'Potato', 'C': 'Tomato'}
    expected_columns = ['Count', 'Percentage']
    df = task_func(vegetable_dict)

    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == expected_columns
    assert len(df) == len(vegetable_dict)
    assert all(df['Count'].between(1, 10))
    assert df['Percentage'].sum() == 100.0

def test_task_func_with_custom_seed():
    vegetable_dict = {'X': 'Cabbage', 'Y': 'Spinach'}
    seed = 42
    df1 = task_func(vegetable_dict, seed=seed)
    df2 = task_func(vegetable_dict, seed=seed)

    assert df1.equals(df2), "DataFrames should be equal with the same seed"

def test_task_func_empty_input():
    vegetable_dict = {}
    df = task_func(vegetable_dict)

    assert df.empty, "DataFrame should be empty for empty input"

def test_task_func_all_vegetables():
    vegetable_dict = {str(i): veg for i, veg in enumerate(VEGETABLES)}
    df = task_func(vegetable_dict)

    assert len(df) == len(VEGETABLES)
    assert all(df.index.isin(VEGETABLES)), "All vegetables should be in the DataFrame index"