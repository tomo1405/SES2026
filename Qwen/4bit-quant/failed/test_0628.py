import pytest
from src_0628 import task_func
from statistics import mean
import pandas as pd

def test_task_func():
    # Test with a list of products
    products = ['Product A', 'Product B']
    df = task_func(products)
    
    # Check if the DataFrame has the correct number of rows and columns
    assert len(df) == len(products), "The number of rows in the DataFrame should match the number of products"
    assert len(df.columns) == 14, "The number of columns in the DataFrame should be 14 (1 for Product name and 12 for months plus 1 for Average Sales)"
    
    # Check if the DataFrame contains the correct columns
    expected_columns = ['Product'] + [f'Month {i+1}' for i in range(12)] + ['Average Sales']
    assert all(col in df.columns for col in expected_columns), "The DataFrame should contain the correct columns"
    
    # Check if the average sales are correctly calculated
    for index, row in df.iterrows():
        monthly_sales = row[1:13]
        calculated_avg_sales = mean(monthly_sales)
        assert row['Average Sales'] == calculated_avg_sales, "The Average Sales should match the mean of the monthly sales"

# Additional test to check if the function handles an empty list of products
def test_task_func_empty_products():
    products = []
    df = task_func(products)
    
    # Check if the DataFrame is empty
    assert df.empty, "The DataFrame should be empty when the input list is empty"

# Additional test to check if the function handles a single product
def test_task_func_single_product():
    products = ['Product C']
    df = task_func(products)
    
    # Check if the DataFrame has the correct number of rows and columns
    assert len(df) == 1, "The number of rows in the DataFrame should be 1 for a single product"
    assert len(df.columns) == 14, "The number of columns in the DataFrame should be 14"
    
    # Check if the DataFrame contains the correct columns
    expected_columns = ['Product'] + [f'Month {i+1}' for i in range(12)] + ['Average Sales']
    assert all(col in df.columns for col in expected_columns), "The DataFrame should contain the correct columns"
    
    # Check if the average sales are correctly calculated
    monthly_sales = df.iloc[0, 1:13]
    calculated_avg_sales = mean(monthly_sales)
    assert df.iloc[0, 'Average Sales'] == calculated_avg_sales, "The Average Sales should match the mean of the monthly sales"