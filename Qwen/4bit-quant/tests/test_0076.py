from datetime import datetime

import pandas as pd
import pytest
import seaborn as sns
from src_0076 import task_func


def test_task_func_input_type():
    with pytest.raises(TypeError):
        task_func("not_a_dataframe")

def test_task_func_empty_dataframe():
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_sales_bounds():
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df, sales_lower_bound=50, sales_upper_bound=50)

def test_task_func_default_values():
    df = pd.DataFrame()
    result_df, plot = task_func(df)
    assert isinstance(result_df, pd.DataFrame)
    assert isinstance(plot, sns.axisgrid.FacetGrid)
    assert len(result_df) == 35  # 5 fruits * 7 days

def test_task_func_custom_fruits_and_days():
    df = pd.DataFrame()
    fruits = ['Grape', 'Lemon']
    days = [datetime(2024, 1, 1), datetime(2024, 1, 2)]
    result_df, plot = task_func(df, fruits=fruits, days=days)
    assert len(result_df) == 4  # 2 fruits * 2 days

def test_task_func_seed():
    df = pd.DataFrame()
    result_df1, _ = task_func(df, seed=42)
    result_df2, _ = task_func(df, seed=42)
    assert result_df1.equals(result_df2)

def test_task_func_sales_range():
    df = pd.DataFrame()
    result_df, _ = task_func(df, sales_lower_bound=1, sales_upper_bound=10)
    assert (result_df['Sales'] >= 1).all() and (result_df['Sales'] < 10).all()