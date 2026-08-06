import pytest
from src_0943 import task_func
import pandas as pd
import numpy as np

def test_task_func_default_parameters():
    sales_df, ax = task_func()
    assert isinstance(sales_df, pd.DataFrame)
    assert sales_df.shape == (PERIODS * len(CATEGORIES), 3)
    assert all(col in sales_df.columns for col in ['Date', 'Category', 'Sales'])
    assert isinstance(ax, plt.Axes)

def test_task_func_custom_parameters():
    custom_start_date = '2020-01-01'
    custom_periods = 5
    custom_freq = 'WOM-1FRI'
    custom_categories = ['Books', 'Toys']
    sales_df, ax = task_func(custom_start_date, custom_periods, custom_freq, custom_categories)
    assert isinstance(sales_df, pd.DataFrame)
    assert sales_df.shape == (custom_periods * len(custom_categories), 3)
    assert all(col in sales_df.columns for col in ['Date', 'Category', 'Sales'])
    assert isinstance(ax, plt.Axes)

def test_task_func_reproducibility():
    sales_df1, _ = task_func()
    sales_df2, _ = task_func()
    assert sales_df1.equals(sales_df2)

def test_task_func_date_range():
    sales_df, _ = task_func()
    date_range = pd.date_range(start=START_DATE, periods=PERIODS, freq=FREQ)
    assert all(date in sales_df['Date'].values for date in date_range)

def test_task_func_categories():
    sales_df, _ = task_func()
    assert all(category in sales_df['Category'].values for category in CATEGORIES)