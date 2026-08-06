import pytest
from src_0352 import task_func
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
    expected_columns = ['Product', 'Category', 'Quantity Sold', 'Revenue']
    assert list(result.columns) == expected_columns

def test_task_func_row_count():
    product_list = ['ProductA', 'ProductB']
    categories = ['Category1', 'Category2']
    result = task_func(product_list, categories)
    assert len(result) == len(product_list)

def test_task_func_quantity_sold_range():
    product_list = ['ProductA', 'ProductB']
    categories = ['Category1', 'Category2']
    min_value = 10
    max_value = 100
    result = task_func(product_list, categories, min_value, max_value)
    assert all(min_value <= row['Quantity Sold'] <= max_value for index, row in result.iterrows())

def test_task_func_revenue_calculation():
    product_list = ['ProductA', 'ProductB']
    categories = ['Category1', 'Category2']
    min_value = 10
    max_value = 100
    result = task_func(product_list, categories, min_value, max_value)
    for index, row in result.iterrows():
        assert row['Revenue'] == row['Quantity Sold'] * random.randint(min_value, max_value)

def test_task_func_default_parameters():
    product_list = ['ProductA', 'ProductB']
    categories = ['Category1', 'Category2']
    result = task_func(product_list, categories)
    assert result.equals(task_func(product_list, categories, 10, 100))