import pytest
from src_0946 import task_func
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def test_task_func_default_parameters():
    future_sales = task_func()
    assert len(future_sales) == 13
    assert all(isinstance(x, float) for x in future_sales)

def test_task_func_custom_parameters():
    start_date = '2020-01-01'
    periods = 5
    freq = 'D'
    future_sales = task_func(start_date=start_date, periods=periods, freq=freq)
    assert len(future_sales) == periods
    assert all(isinstance(x, float) for x in future_sales)

def test_task_func_with_sales_data():
    sales_data = np.array([150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750])
    future_sales = task_func(sales_data=sales_data)
    assert len(future_sales) == 13
    assert all(isinstance(x, float) for x in future_sales)

def test_task_func_linear_regression_fit():
    future_sales = task_func()
    assert isinstance(future_sales, np.ndarray)
    assert future_sales.shape == (13,)
    assert all(isinstance(x, float) for x in future_sales)

def test_task_func_date_range():
    start_date = '2016-01-01'
    periods = 13
    freq = 'WOM-2FRI'
    date_range = pd.date_range(start=start_date, freq=freq, periods=periods)
    assert len(date_range) == periods
    assert isinstance(date_range[0], pd.Timestamp)

def test_task_func_dataframe_creation():
    sales_data = np.random.randint(low=100, high=500, size=13)
    date_range = pd.date_range(start='2016-01-01', freq='WOM-2FRI', periods=13)
    sales_df = pd.DataFrame({'Date': date_range, 'Sales': sales_data})
    assert sales_df.shape == (13, 2)
    assert 'Date' in sales_df.columns
    assert 'Sales' in sales_df.columns

def test_task_func_model_prediction():
    sales_data = np.random.randint(low=100, high=500, size=13)
    X = np.arange(13).reshape(-1, 1)
    y = sales_data
    model = LinearRegression()
    model.fit(X, y)
    future_dates = np.arange(13, 26).reshape(-1, 1)
    future_sales = model.predict(future_dates)
    assert len(future_sales) == 13
    assert all(isinstance(x, float) for x in future_sales)