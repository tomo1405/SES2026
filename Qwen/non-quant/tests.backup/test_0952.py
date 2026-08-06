import pytest
from src_0952 import task_func
import pandas as pd
import numpy as np

def test_task_func_output_type():
    mystrings = ["Laptop", "Jeans", "Microwave"]
    n_products = 5
    result = task_func(mystrings, n_products)
    assert isinstance(result, pd.DataFrame)

def test_task_func_column_names():
    mystrings = ["Laptop", "Jeans", "Microwave"]
    n_products = 5
    result = task_func(mystrings, n_products)
    expected_columns = ['Product Name', 'Category', 'Price']
    assert list(result.columns) == expected_columns

def test_task_func_number_of_rows():
    mystrings = ["Laptop", "Jeans", "Microwave"]
    n_products = 5
    result = task_func(mystrings, n_products)
    assert len(result) == n_products

def test_task_func_product_name_format():
    mystrings = ["Laptop", "Jeans", "Microwave"]
    n_products = 5
    result = task_func(mystrings, n_products)
    for name in result['Product Name']:
        assert isinstance(name, str)
        assert ' ' not in name

def test_task_func_category_values():
    mystrings = ["Laptop", "Jeans", "Microwave"]
    n_products = 5
    result = task_func(mystrings, n_products)
    for category in result['Category']:
        assert category in ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Toys & Games']

def test_task_func_price_range():
    mystrings = ["Laptop", "Jeans", "Microwave"]
    n_products = 5
    result = task_func(mystrings, n_products)
    for price in result['Price']:
        assert 30 <= price <= 70

def test_task_func_reproducibility():
    mystrings = ["Laptop", "Jeans", "Microwave"]
    n_products = 5
    seed_value = 42
    first_run = task_func(mystrings, n_products, seed_value)
    second_run = task_func(mystrings, n_products, seed_value)
    assert first_run.equals(second_run)