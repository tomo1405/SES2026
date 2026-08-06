import pytest
from src_0076 import task_func
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def test_task_func_type_error():
    with pytest.raises(TypeError):
        task_func("not_a_dataframe")

def test_task_func_value_error_non_empty_df():
    df = pd.DataFrame({'Fruit': ['Apple'], 'Day': [datetime(2024, 1, 1)], 'Sales': [10]})
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_value_error_sales_bounds():
    with pytest.raises(ValueError):
        task_func(pd.DataFrame(), sales_lower_bound=50, sales_upper_bound=1)

def test_task_func_default_fruits_and_days():
    df = pd.DataFrame()
    result_df, plot = task_func(df)
    assert result_df.shape == (35, 3)  # 5 fruits * 7 days
    assert all(result_df['Fruit'].isin(['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']))
    assert all(result_df['Day'] >= datetime(2024, 1, 1)) and all(result_df['Day'] <= datetime(2024, 1, 7))
    assert result_df['Sales'].between(1, 50).all()

def test_task_func_custom_fruits_and_days():
    df = pd.DataFrame()
    fruits = ['Kiwi', 'Mango']
    days = [datetime(2024, 1, 8), datetime(2024, 1, 9)]
    result_df, plot = task_func(df, fruits=fruits, days=days)
    assert result_df.shape == (4, 3)  # 2 fruits * 2 days
    assert all(result_df['Fruit'].isin(['Kiwi', 'Mango']))
    assert all(result_df['Day'] >= datetime(2024, 1, 8)) and all(result_df['Day'] <= datetime(2024, 1, 9))

def test_task_func_seed():
    df = pd.DataFrame()
    seed = 42
    result_df1, _ = task_func(df, seed=seed)
    result_df2, _ = task_func(df, seed=seed)
    assert result_df1.equals(result_df2)

def test_task_func_sales_bounds():
    df = pd.DataFrame()
    result_df, plot = task_func(df, sales_lower_bound=10, sales_upper_bound=20)
    assert result_df['Sales'].between(10, 20).all()