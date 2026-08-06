import pandas as pd
from src_0952 import task_func


def test_task_func():
    mystrings = ['Product 1', 'Product 2', 'Product 3']
    n_products = 3
    seed = 0
    expected_output = pd.DataFrame([['Product_1', 'Electronics', 50.0],
                                  ['Product_2', 'Clothing', 50.0],
                                  ['Product_3', 'Home & Kitchen', 50.0]],
                                 columns=['Product Name', 'Category', 'Price'])

    output = task_func(mystrings, n_products, seed)

    assert output.equals(expected_output)