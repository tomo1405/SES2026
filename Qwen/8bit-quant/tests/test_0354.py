import pandas as pd
import pytest
from src_0354 import task_func


def test_task_func_basic():
    product_list = ['Product A', 'Product B']
    categories = ['Category X', 'Category Y']
    df = task_func(product_list, categories)
    
    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(product_list)
    assert list(df.columns) == ['Product', 'Category', 'Quantity Sold', 'Revenue', 'Total Revenue']

def test_task_func_min_max_values():
    product_list = ['Product A']
    categories = ['Category X']
    min_value = 20
    max_value = 80
    df = task_func(product_list, categories, min_value, max_value)
    
    assert df['Quantity Sold'].min() >= min_value
    assert df['Quantity Sold'].max() <= max_value
    assert df['Revenue'].min() >= min_value
    assert df['Revenue'].max() <= max_value
    assert df['Total Revenue'].min() >= min_value * min_value
    assert df['Total Revenue'].max() <= max_value * max_value

def test_task_func_empty_product_list():
    product_list = []
    categories = ['Category X', 'Category Y']
    df = task_func(product_list, categories)
    
    assert df.empty

def test_task_func_empty_categories():
    product_list = ['Product A', 'Product B']
    categories = []
    with pytest.raises(IndexError):
        task_func(product_list, categories)

def test_task_func_single_product_category():
    product_list = ['Product A']
    categories = ['Category X']
    df = task_func(product_list, categories)
    
    assert len(df) == 1
    assert df['Category'].iloc[0] == categories[0]

def test_task_func_large_product_list():
    product_list = [f'Product {i}' for i in range(100)]
    categories = ['Category X', 'Category Y']
    df = task_func(product_list, categories)
    
    assert len(df) == len(product_list)