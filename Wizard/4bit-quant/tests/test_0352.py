python
import pandas as pd
import random
import pytest

def task_func(product_list, categories, min_value=10, max_value=100):
    report_data = []
    for product in product_list:
        category = categories[random.randint(0, len(categories)-1)]
        quantity_sold = random.randint(min_value, max_value)
        revenue = quantity_sold * random.randint(min_value, max_value)
        report_data.append([product, category, quantity_sold, revenue])
    report_df = pd.DataFrame(report_data, columns=['Product', 'Category', 'Quantity Sold', 'Revenue'])
    return report_df

def test_task_func():
    product_list = ['Product A', 'Product B', 'Product C']
    categories = ['Category A', 'Category B', 'Category C']
    report_df = task_func(product_list, categories)
    assert report_df.shape == (3, 4)
    assert report_df.columns.tolist() == ['Product', 'Category', 'Quantity Sold', 'Revenue']
    assert report_df['Product'].tolist() == product_list
    assert report_df['Category'].tolist() == categories
    assert report_df['Quantity Sold'].min() >= 10
    assert report_df['Quantity Sold'].max() <= 100
    assert report_df['Revenue'].min() >= 1000
    assert report_df['Revenue'].max() <= 10000