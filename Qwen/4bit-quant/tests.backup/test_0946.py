import pytest
from src_0946 import task_func
import numpy as np
import pandas as pd

def test_task_func_default_parameters():
    future_sales = task_func()
    assert isinstance(future_sales, np.ndarray)
    assert future_sales.shape == (13,)

def test_task_func_custom_start_date():
    future_sales = task_func(start_date='2020-01-01')
    assert isinstance(future_sales, np.ndarray)
    assert future_sales.shape == (13,)

def test_task_func_custom_periods():
    future_sales = task_func(periods=20)
    assert isinstance(future_sales, np.ndarray)
    assert future_sales.shape == (20,)

def test_task_func_custom_freq():
    future_sales = task_func(freq='WOM-3MON')
    assert isinstance(future_sales, np.ndarray)
    assert future_sales.shape == (13,)

def test_task_func_with_sales_data():
    sales_data = np.array([100, 200, 300, 400, 500])
    future_sales = task_func(sales_data=sales_data)
    assert isinstance(future_sales, np.ndarray)
    assert future_sales.shape == (13,)

def test_task_func_with_different_seed():
    np.random.seed(0)
    future_sales_1 = task_func()
    np.random.seed(0)
    future_sales_2 = task_func()
    assert np.array_equal(future_sales_1, future_sales_2)

def test_task_func_date_range():
    future_sales = task_func()
    date_range = pd.date_range(start='2016-01-01', freq='WOM-2FRI', periods=13)
    assert len(date_range) == 13

def test_task_func_model_fit():
    future_sales = task_func()
    assert len(future_sales) == 13