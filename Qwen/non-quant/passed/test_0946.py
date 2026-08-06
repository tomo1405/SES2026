import pytest
from src_0946 import task_func
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def test_task_func_default_parameters():
    future_sales = task_func()
    assert isinstance(future_sales, np.ndarray)
    assert len(future_sales) == 13

def test_task_func_custom_start_date():
    future_sales = task_func(start_date='2020-01-01')
    assert isinstance(future_sales, np.ndarray)
    assert len(future_sales) == 13

def test_task_func_custom_periods():
    future_sales = task_func(periods=20)
    assert isinstance(future_sales, np.ndarray)
    assert len(future_sales) == 20

def test_task_func_custom_freq():
    future_sales = task_func(freq='WOM-3FRI')
    assert isinstance(future_sales, np.ndarray)
    assert len(future_sales) == 13

def test_task_func_with_sales_data():
    sales_data = np.array([150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750])
    future_sales = task_func(sales_data=sales_data)
    assert isinstance(future_sales, np.ndarray)
    assert len(future_sales) == 13

def test_task_func_model_fit():
    future_sales = task_func()
    assert isinstance(future_sales, np.ndarray)
    assert len(future_sales) == 13

def test_task_func_future_dates_prediction():
    future_sales = task_func()
    assert isinstance(future_sales, np.ndarray)
    assert len(future_sales) == 13