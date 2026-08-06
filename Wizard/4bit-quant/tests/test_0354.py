python
import pandas as pd
import random
import pytest

def task_func(product_list, categories, min_value=10, max_value=100):
    report_data = []

    for product in product_list:
        category = categories[random.randint(0, len(categories)-1)]
        quantity_sold = random.randint(min_value, max_value)
        revenue = random.randint(min_value, max_value)
        total_revenue = quantity_sold * revenue
        report_data.append([product, category, quantity_sold, revenue, total_revenue])

    report_df = pd.DataFrame(report_data, columns=['Product', 'Category', 'Quantity Sold', 'Revenue', 'Total Revenue'])
    return report_df

def test_task_func():
    product_list = ['Product A', 'Product B', 'Product C']
    categories = ['Category A', 'Category B', 'Category C']

    report_df = task_func(product_list, categories)

    assert report_df.shape == (3, 5)
    assert report_df.columns.tolist() == ['Product', 'Category', 'Quantity Sold', 'Revenue', 'Total Revenue']
    assert report_df['Product'].tolist() == product_list
    assert report_df['Category'].tolist() == categories
    assert all(report_df['Quantity Sold'] >= 10)
    assert all(report_df['Quantity Sold'] <= 100)
    assert all(report_df['Revenue'] >= 10)
    assert all(report_df['Revenue'] <= 100)
    assert all(report_df['Total Revenue'] >= 1000)
    assert all(report_df['Total Revenue'] <= 10000)