import pytest
from src_0350 import task_func

def test_task_func():
    product_list = ['Product 1', 'Product 2', 'Product 3']
    categories = ['Category 1', 'Category 2', 'Category 3']
    report_df = task_func(product_list, categories)
    assert report_df.columns.tolist() == ['Product', 'Category', 'Quantity Sold', 'Revenue']
    assert len(report_df) == len(product_list)
    assert all(report_df['Product'].isin(product_list))
    assert all(report_df['Category'].isin(categories))
    assert all(report_df['Quantity Sold'] >= 1)
    assert all(report_df['Quantity Sold'] <= 100)
    assert all(report_df['Revenue'] >= 10)
    assert all(report_df['Revenue'] <= 100)