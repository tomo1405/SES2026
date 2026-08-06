import pytest
from src_0352 import task_func

def test_task_func():
    product_list = ['Product 1', 'Product 2', 'Product 3']
    categories = ['Category 1', 'Category 2', 'Category 3']
    min_value = 10
    max_value = 100

    report_df = task_func(product_list, categories, min_value, max_value)

    assert report_df.columns.tolist() == ['Product', 'Category', 'Quantity Sold', 'Revenue']
    assert len(report_df) == len(product_list)
    assert all(report_df['Product'].isin(product_list))
    assert all(report_df['Category'].isin(categories))
    assert all(report_df['Quantity Sold'] >= min_value)
    assert all(report_df['Quantity Sold'] <= max_value)
    assert all(report_df['Revenue'] >= min_value)
    assert all(report_df['Revenue'] <= max_value)