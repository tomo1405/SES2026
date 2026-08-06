import pytest
from src_0350 import task_func
import pandas as pd

def test_task_func():
    # Test with a small list of products and categories
    product_list = ['Product A', 'Product B']
    categories = ['Category X', 'Category Y']

    # Call the function
    report_df = task_func(product_list, categories)

    # Check if the DataFrame has the correct columns
    assert all(col in report_df.columns for col in ['Product', 'Category', 'Quantity Sold', 'Revenue'])

    # Check if the number of rows is equal to the length of the product list
    assert len(report_df) == len(product_list)

    # Check if the 'Product' column contains the correct values
    assert set(report_df['Product']) == set(product_list)

    # Check if the 'Category' column contains values from the categories list
    assert all(category in categories for category in report_df['Category'])

    # Check if 'Quantity Sold' and 'Revenue' are within the expected range
    for index, row in report_df.iterrows():
        assert 1 <= row['Quantity Sold'] <= 100
        assert 10 <= row['Revenue'] / row['Quantity Sold'] <= 100

    # Test with an empty product list
    product_list_empty = []
    report_df_empty = task_func(product_list_empty, categories)

    # Check if the DataFrame is empty
    assert report_df_empty.empty

    # Test with an empty category list (should raise an error)
    with pytest.raises(IndexError):
        task_func(product_list, [])