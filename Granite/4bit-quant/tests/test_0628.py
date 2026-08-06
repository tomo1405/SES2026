import pytest
from src_0628 import task_func
from random import randint
from statistics import mean
import pandas as pd

@pytest.fixture
def products_list():
    return ['Product 1', 'Product 2', 'Product 3']

def test_task_func(products_list):
    sales_data = []

    for product in products_list:
        sales = [randint(100, 500) for _ in range(12)]
        avg_sales = mean(sales)
        sales.append(avg_sales)
        sales_data.append([product] + sales)

    sales_df = pd.DataFrame(sales_data, columns=['Product'] + [f'Month {i+1}' for i in range(12)] + ['Average Sales'])

    assert task_func(products_list).equals(sales_df)

def test_task_func_with_empty_list(products_list):
    assert task_func([]) is None

def test_task_func_with_invalid_input(products_list):
    with pytest.raises(TypeError):
        task_func(123)