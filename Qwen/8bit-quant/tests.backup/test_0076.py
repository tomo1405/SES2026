import pytest
from src_0076 import task_func
import pandas as pd
import numpy as np

def test_task_func_input_type():
    with pytest.raises(TypeError):
        task_func("not a dataframe")

def test_task_func_empty_dataframe():
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_sales_bounds():
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df, sales_lower_bound=50, sales_upper_bound=1)

def test_task_func_default_fruits_and_days():
    df = pd.DataFrame()
    result_df, plot = task_func(df)
    assert result_df.shape == (35, 3)  # 5 fruits * 7 days
    assert all(result_df['Fruit'].isin(['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']))
    assert all(result_df['Day'] >= datetime(2024, 1, 1)) and all(result_df['Day'] <= datetime(2024, 1, 7))

def test_task_func_custom_fruits_and_days():
    df = pd.DataFrame()
    fruits = ['Grape', 'Kiwi']
    days = [datetime(2024, 1, 8) + timedelta(days=x) for x in range(2)]
    result_df, plot = task_func(df, fruits=fruits, days=days)
    assert result_df.shape == (4, 3)  # 2 fruits * 2 days
    assert all(result_df['Fruit'].isin(['Grape', 'Kiwi']))
    assert all(result_df['Day'] >= datetime(2024, 1, 8)) and all(result_df['Day'] <= datetime(2024, 1, 9))

def test_task_func_seed_reproducibility():
    df = pd.DataFrame()
    seed = 42
    result_df1, _ = task_func(df, seed=seed)
    result_df2, _ = task_func(df, seed=seed)
    assert result_df1.equals(result_df2)

def test_task_func_sales_range():
    df = pd.DataFrame()
    result_df, _ = task_func(df, sales_lower_bound=10, sales_upper_bound=20)
    assert result_df['Sales'].min() >= 10
    assert result_df['Sales'].max() <= 20