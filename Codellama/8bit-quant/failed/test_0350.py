import pytest
from src_0350 import task_func

def test_task_func():
    product_list = ['Product 1', 'Product 2', 'Product 3']
    categories = ['Category 1', 'Category 2', 'Category 3']
    report_df = task_func(product_list, categories)
    assert report_df.shape == (3, 4)
    assert report_df.columns.tolist() == ['Product', 'Category', 'Quantity Sold', 'Revenue']
    assert report_df['Product'].tolist() == product_list
    assert report_df['Category'].tolist() == categories
    assert report_df['Quantity Sold'].tolist() == [random.randint(1, 100) for _ in range(3)]
    assert report_df['Revenue'].tolist() == [random.randint(10, 100) for _ in range(3)]