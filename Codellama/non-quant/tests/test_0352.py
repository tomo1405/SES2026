import random

from src_0352 import task_func


def test_task_func():
    product_list = ['Product 1', 'Product 2', 'Product 3']
    categories = ['Category 1', 'Category 2', 'Category 3']
    min_value = 10
    max_value = 100

    report_df = task_func(product_list, categories, min_value, max_value)

    assert report_df.shape == (3, 4)
    assert report_df.columns.tolist() == ['Product', 'Category', 'Quantity Sold', 'Revenue']
    assert report_df['Product'].tolist() == product_list
    assert report_df['Category'].tolist() == categories
    assert report_df['Quantity Sold'].tolist() == [random.randint(min_value, max_value) for _ in range(3)]
    assert report_df['Revenue'].tolist() == [random.randint(min_value, max_value) for _ in range(3)]