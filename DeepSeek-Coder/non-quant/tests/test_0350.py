import pytest
from src_0350 import task_func
import pandas as pd
import random

def test_task_func():
    # Test the function with a sample input
    product_list = ['Product1', 'Product2', 'Product3']
    categories = ['CategoryA', 'CategoryB', 'CategoryC']
    
    result = task_func(product_list=product_list, categories=categories)
    
    # Check if the result is a DataFrame
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    
    # Check if the DataFrame has the correct columns
    expected_columns = ['Product', 'Category', 'Quantity Sold', 'Revenue']
    assert list(result.columns) == expected_columns, "The DataFrame columns are incorrect"
    
    # Add more assertions to check the content of the DataFrame if necessary