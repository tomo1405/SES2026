python
import pandas as pd
import random
import pytest

def task_func(product_list, categories):

    report_data = []

    for product in product_list:
        category = categories[random.randint(0, len(categories)-1)]
        quantity_sold = random.randint(1, 100)
        revenue = quantity_sold * random.randint(10, 100)
        report_data.append([product, category, quantity_sold, revenue])

    report_df = pd.DataFrame(report_data, columns=['Product', 'Category', 'Quantity Sold', 'Revenue'])
    return report_df

def test_task_func():
    categories = ['Electronics', 'Clothing', 'Home Appliances']
    product_list = ['iPhone', 'Samsung Galaxy', 'Sony TV']

    report_df = task_func(product_list, categories)

    assert report_df.shape == (3, 4)
    assert report_df.columns.tolist() == ['Product', 'Category', 'Quantity Sold', 'Revenue']
    assert report_df['Product'].tolist() == product_list
    assert report_df['Category'].tolist() == [categories[random.randint(0, len(categories)-1)] for _ in range(3)]
    assert report_df['Quantity Sold'].tolist() == [random.randint(1, 100) for _ in range(3)]
    assert report_df['Revenue'].tolist() == [random.randint(10, 100) * random.randint(1, 100) for _ in range(3)]