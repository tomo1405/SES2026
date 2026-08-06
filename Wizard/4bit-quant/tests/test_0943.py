python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pytest

# Constants
START_DATE = '2016-01-01'
PERIODS = 13
FREQ = 'WOM-2FRI'
CATEGORIES = ['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports']

# Import the function to be tested
from src_0943 import task_func

# Test the function
def test_task_func():
    # Ensure reproducible sales figures
    np.random.seed(0)
    
    # Generate sales data
    sales_data = task_func(start_date=START_DATE, periods=PERIODS, freq=FREQ, categories=CATEGORIES)
    
    # Check if the sales data is a tuple of two dataframes
    assert isinstance(sales_data, tuple)
    assert len(sales_data) == 2
    
    # Check if the sales dataframe has the correct columns
    sales_df = sales_data[0]
    assert isinstance(sales_df, pd.DataFrame)
    assert list(sales_df.columns) == ['Date', 'Category', 'Sales']
    
    # Check if the sales dataframe has the correct number of rows
    assert len(sales_df) == PERIODS * len(CATEGORIES)
    
    # Check if the sales dataframe has the correct data types
    assert sales_df['Date'].dtype == 'datetime64[ns]'
    assert sales_df['Category'].dtype == 'object'
    assert sales_df['Sales'].dtype == 'int64'
    
    # Check if the sales dataframe has the correct values
    for i in range(len(sales_df)):
        row = sales_df.iloc[i]
        assert row['Date'].strftime('%Y-%m-%d') == row['Date'].strftime('%Y-%m-%d')
        assert row['Category'] in CATEGORIES
        assert 100 <= row['Sales'] <= 500
    
    # Check if the sales dataframe is sorted by date and category
    assert sales_df.groupby(['Date', 'Category']).ngroups == len(sales_df)
    
    # Check if the sales dataframe has the correct shape
    assert sales_df.pivot(index='Date', columns='Category', values='Sales').shape == (PERIODS, len(CATEGORIES))
    
    # Check if the sales dataframe has the correct values
    for i in range(len(sales_df)):
        row = sales_df.iloc[i]
        assert sales_df.pivot(index='Date', columns='Category', values='Sales').iloc[row['Date'].dayofweek, CATEGORIES.index(row['Category'])] == row['Sales']
    
    # Check if the plot has the correct title and grid
    fig, ax = sales_data[1]
    assert ax.get_title() == 'Category-wise Sales Trends'
    assert ax.get_xlabel() == 'Date'
    assert ax.get_ylabel() == 'Sales'
    assert ax.get_ylim() == (0, 500)
    assert ax.get_xlim() == (pd.to_datetime(START_DATE), pd.to_datetime(START_DATE) + pd.DateOffset(days=PERIODS*7))
    assert ax.get_xticks().shape == (PERIODS*7,)
    assert ax.get_yticks().shape == (5,)
    assert ax.grid()