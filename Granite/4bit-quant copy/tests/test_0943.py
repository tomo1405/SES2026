import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from src_0943 import task_func
import pytest

@pytest.fixture
def sales_df():
    np.random.seed(0)  # Ensure reproducible sales figures
    date_range = pd.date_range(start='2016-01-01', periods=13, freq='WOM-2FRI')
    report_data = []

    for date in date_range:
        for category in ['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports']:
            sales = np.random.randint(low=100, high=500)
            report_data.append([date, category, sales])

    return pd.DataFrame(report_data, columns=['Date', 'Category', 'Sales'])

def test_task_func(sales_df):
    sales_df, ax = task_func()
    assert isinstance(sales_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert sales_df.shape == (13, 6)
    assert list(sales_df.columns) == ['Date', 'Category', 'Sales']
    assert ax.get_title() == 'Category-wise Sales Trends'

def test_task_func_with_custom_args(sales_df):
    custom_start_date = '2022-01-01'
    custom_periods = 26
    custom_freq = 'WOM-3FRI'
    custom_categories = ['Books', 'Toys', 'Grocery', 'Jewelry']
    sales_df, ax = task_func(custom_start_date, custom_periods, custom_freq, custom_categories)
    assert isinstance(sales_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert sales_df.shape == (26, 5)
    assert list(sales_df.columns) == ['Date', 'Category', 'Sales']
    assert ax.get_title() == 'Category-wise Sales Trends'