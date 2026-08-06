import pytest
from src_0076 import task_func
import pandas as pd
import numpy as np
import itertools
from datetime import datetime, timedelta
import seaborn as sns

def test_task_func_input_not_dataframe():
    with pytest.raises(TypeError):
        task_func(1)

def test_task_func_input_dataframe_not_empty():
    df = pd.DataFrame({'A': [1, 2, 3]})
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_sales_lower_bound_greater_than_upper_bound():
    with pytest.raises(ValueError):
        task_func(pd.DataFrame(), sales_lower_bound=50, sales_upper_bound=1)

def test_task_func_fruits_none():
    df = pd.DataFrame()
    result_df, plot = task_func(df)
    assert result_df.shape == (25, 3)
    assert plot.shape == (25, 3)

def test_task_func_days_none():
    df = pd.DataFrame()
    result_df, plot = task_func(df, days=None)
    assert result_df.shape == (25, 3)
    assert plot.shape == (25, 3)

def test_task_func_seed_not_none():
    df = pd.DataFrame()
    result_df, plot = task_func(df, seed=123)
    assert result_df.shape == (25, 3)
    assert plot.shape == (25, 3)

def test_task_func_sales_lower_bound_and_upper_bound():
    df = pd.DataFrame()
    result_df, plot = task_func(df, sales_lower_bound=10, sales_upper_bound=50)
    assert result_df.shape == (25, 3)
    assert plot.shape == (25, 3)

def test_task_func_fruits_and_days():
    df = pd.DataFrame()
    result_df, plot = task_func(df, fruits=['Apple', 'Banana'], days=[datetime(2024, 1, 1), datetime(2024, 1, 2)])
    assert result_df.shape == (2, 3)
    assert plot.shape == (2, 3)

def test_task_func_fruits_and_days_and_seed():
    df = pd.DataFrame()
    result_df, plot = task_func(df, fruits=['Apple', 'Banana'], days=[datetime(2024, 1, 1), datetime(2024, 1, 2)], seed=123)
    assert result_df.shape == (2, 3)
    assert plot.shape == (2, 3)

def test_task_func_fruits_and_days_and_sales_lower_bound_and_upper_bound():
    df = pd.DataFrame()
    result_df, plot = task_func(df, fruits=['Apple', 'Banana'], days=[datetime(2024, 1, 1), datetime(2024, 1, 2)], sales_lower_bound=10, sales_upper_bound=50)
    assert result_df.shape == (2, 3)
    assert plot.shape == (2, 3)

def test_task_func_fruits_and_days_and_sales_lower_bound_and_upper_bound_and_seed():
    df = pd.DataFrame()
    result_df, plot = task_func(df, fruits=['Apple', 'Banana'], days=[datetime(2024, 1, 1), datetime(2024, 1, 2)], sales_lower_bound=10, sales_upper_bound=50, seed=123)
    assert result_df.shape == (2, 3)
    assert plot.shape == (2, 3)