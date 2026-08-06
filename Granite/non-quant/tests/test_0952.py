import pandas as pd
import numpy as np
import random
from random import randint, seed
from src_0952 import task_func

def test_task_func():
    mystrings = ['Product 1', 'Product 2', 'Product 3']
    n_products = 5
    seed(0)
    catalogue_df = task_func(mystrings, n_products)
    assert isinstance(catalogue_df, pd.DataFrame)
    assert catalogue_df.shape == (n_products, 3)
    assert catalogue_df['Product Name'].dtype == 'object'
    assert catalogue_df['Category'].dtype == 'object'
    assert catalogue_df['Price'].dtype == 'float64'
    expected_categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Toys & Games']
    for category in catalogue_df['Category']:
        assert category in expected_categories
    expected_product_names = ['Product_1', 'Product_2', 'Product_3']
    for product_name in catalogue_df['Product Name']:
        assert product_name in expected_product_names