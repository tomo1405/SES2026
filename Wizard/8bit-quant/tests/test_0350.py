python
import pandas as pd
import random
import pytest

from src_0350 import task_func

def test_task_func():
    product_list = ['Product A', 'Product B', 'Product C']
    categories = ['Category 1', 'Category 2', 'Category 3']

    report_data = []

    for product in product_list:
        category = categories[random.randint(0, len(categories)-1)]
        quantity_sold = random.randint(1, 100)
        revenue = quantity_sold * random.randint(10, 100)
        report_data.append([product, category, quantity_sold, revenue])

    report_df = pd.DataFrame(report_data, columns=['Product', 'Category', 'Quantity Sold', 'Revenue'])

    assert task_func(product_list, categories).equals(report_df)