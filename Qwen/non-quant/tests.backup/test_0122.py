import pytest
from src_0122 import task_func
import pandas as pd
import numpy as np

def test_task_func_input_type():
    with pytest.raises(TypeError):
        task_func("not a list")

def test_task_func_output_type():
    df, ax = task_func([1, 2, 3])
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)

def test_task_func_dataframe_columns():
    df, _ = task_func([1, 2, 3])
    assert list(df.columns) == ['Category', 'Sales']

def test_task_func_dataframe_length():
    df, _ = task_func([1, 2, 3])
    assert len(df) == 5

def test_task_func_randomness():
    df1, _ = task_func([1, 2, 3], seed=42)
    df2, _ = task_func([1, 2, 3], seed=42)
    assert df1.equals(df2)

def test_task_func_appended_value():
    df, _ = task_func([1, 2, 3])
    assert df['Sales'].iloc[-1] == 1200  # Since 12 * 100 = 1200

def test_task_func_categories():
    df, _ = task_func([1, 2, 3])
    assert all(category in df['Category'].values for category in ['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports'])