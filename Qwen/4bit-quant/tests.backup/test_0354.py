import pytest
from src_0354 import task_func

def test_task_func_with_default_values():
    product_list = ['ProductA', 'ProductB']
    categories = ['Category1', 'Category2']
    
    df = task_func(product_list, categories)
    
    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(product_list)
    assert all(column in df.columns for column in ['Product', 'Category', 'Quantity Sold', 'Revenue', 'Total Revenue'])

def test_task_func_with_custom_min_max_values():
    product_list = ['ProductC']
    categories = ['Category3']
    min_value = 5
    max_value = 20
    
    df = task_func(product_list, categories, min_value, max_value)
    
    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(product_list)
    assert all(column in df.columns for column in ['Product', 'Category', 'Quantity Sold', 'Revenue', 'Total Revenue'])
    assert all(df['Quantity Sold'].between(min_value, max_value))
    assert all(df['Revenue'].between(min_value, max_value))

def test_task_func_with_empty_product_list():
    product_list = []
    categories = ['Category4']
    
    df = task_func(product_list, categories)
    
    assert isinstance(df, pd.DataFrame)
    assert df.empty

def test_task_func_with_single_category():
    product_list = ['ProductD', 'ProductE']
    categories = ['Category5']
    
    df = task_func(product_list, categories)
    
    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(product_list)
    assert all(df['Category'] == categories[0])