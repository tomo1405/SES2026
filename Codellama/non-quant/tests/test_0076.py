from datetime import datetime

import pandas as pd
import pytest
from src_0076 import task_func


def test_task_func_input_type():
    df = pd.DataFrame()
    fruits = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
    days = [datetime(2024, 1, 1) + timedelta(days=x) for x in range(7)]
    seed = None
    sales_lower_bound = 1
    sales_upper_bound = 50

    with pytest.raises(TypeError):
        task_func(df, fruits, days, seed, sales_lower_bound, sales_upper_bound)

def test_task_func_input_empty_df():
    df = pd.DataFrame()
    fruits = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
    days = [datetime(2024, 1, 1) + timedelta(days=x) for x in range(7)]
    seed = None
    sales_lower_bound = 1
    sales_upper_bound = 50

    with pytest.raises(ValueError):
        task_func(df, fruits, days, seed, sales_lower_bound, sales_upper_bound)

def test_task_func_sales_lower_bound():
    df = pd.DataFrame()
    fruits = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
    days = [datetime(2024, 1, 1) + timedelta(days=x) for x in range(7)]
    seed = None
    sales_lower_bound = 50
    sales_upper_bound = 1

    with pytest.raises(ValueError):
        task_func(df, fruits, days, seed, sales_lower_bound, sales_upper_bound)

def test_task_func_output_type():
    df = pd.DataFrame()
    fruits = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
    days = [datetime(2024, 1, 1) + timedelta(days=x) for x in range(7)]
    seed = None
    sales_lower_bound = 1
    sales_upper_bound = 50

    result_df, plot = task_func(df, fruits, days, seed, sales_lower_bound, sales_upper_bound)

    assert isinstance(result_df, pd.DataFrame)
    assert isinstance(plot, sns.boxplot)

def test_task_func_output_data():
    df = pd.DataFrame()
    fruits = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
    days = [datetime(2024, 1, 1) + timedelta(days=x) for x in range(7)]
    seed = None
    sales_lower_bound = 1
    sales_upper_bound = 50

    result_df, plot = task_func(df, fruits, days, seed, sales_lower_bound, sales_upper_bound)

    assert len(result_df) == 5 * 7
    assert result_df['Fruit'].unique().tolist() == fruits
    assert result_df['Day'].unique().tolist() == days
    assert result_df['Sales'].min() >= sales_lower_bound
    assert result_df['Sales'].max() <= sales_upper_bound