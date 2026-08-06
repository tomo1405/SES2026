import pytest
from src_0354 import task_func
import pandas as pd

def test_task_func_output_type():
    product_list = ['ProductA', 'ProductB']
    categories = ['Category1', 'Category2']
    result = task_func(product_list, categories)
    assert isinstance(result, pd.DataFrame)

def test_task_func_columns():
    product_list = ['ProductA', 'ProductB']
    categories = ['Category1', 'Category2']
    result = task_func(product_list, categories)
    expected_columns = ['Product', 'Category', 'Quantity Sold', 'Revenue', 'Total Revenue']
    assert list(result.columns) == expected_columns

def test_task_func_row_count():
    product_list = ['ProductA', 'ProductB']
    categories = ['Category1', 'Category2']
    result = task_func(product_list, categories)
    assert len(result) == len(product_list)

def test_task_func_min_max_values():
    product_list = ['ProductA']
    categories = ['Category1']
    min_value = 10
    max_value = 100
    result = task_func(product_list, categories, min_value, max_value)
    assert (result['Quantity Sold'] >= min_value).all() and (result['Quantity Sold'] <= max_value).all()
    assert (result['Revenue'] >= min_value).all() and (result['Revenue'] <= max_value).all()

def test_task_func_total_revenue_calculation():
    product_list = ['ProductA']
    categories = ['Category1']
    min_value = 10
    max_value = 100
    result = task_func(product_list, categories, min_value, max_value)
    assert (result['Total Revenue'] == result['Quantity Sold'] * result['Revenue']).all()