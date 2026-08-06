import pandas as pd
from random import randint
from statistics import mean
from src_0628 import task_func

def test_task_func():
    products_list = ['Product 1', 'Product 2', 'Product 3']
    sales_data = []

    for product in products_list:
        sales = [randint(100, 500) for _ in range(12)]
        avg_sales = mean(sales)
        sales.append(avg_sales)
        sales_data.append([product] + sales)

    expected_df = pd.DataFrame(sales_data, columns=['Product'] + [f'Month {i+1}' for i in range(12)] + ['Average Sales'])
    actual_df = task_func(products_list)

    assert actual_df.equals(expected_df)

def test_task_func_with_empty_list():
    products_list = []
    expected_df = pd.DataFrame(columns=['Product'] + [f'Month {i+1}' for i in range(12)] + ['Average Sales'])
    actual_df = task_func(products_list)

    assert actual_df.equals(expected_df)