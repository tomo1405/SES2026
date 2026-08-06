import pandas as pd
import numpy as np
import random
from random import randint, seed
from src_0952 import task_func

# Constants
CATEGORIES = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Toys & Games']

def test_task_func():
    mystrings = ['Product 1', 'Product 2', 'Product 3']
    n_products = 5
    seed = 0
    random.seed(seed)
    np.random.seed(seed)
    catalogue_data = []
    for _ in range(n_products):
        product_name = mystrings[randint(0, len(mystrings) - 1)].replace(' ', '_')
        category = CATEGORIES[randint(0, len(CATEGORIES) - 1)]
        price = round(np.random.normal(50, 10), 2)
        catalogue_data.append([product_name, category, price])

    catalogue_df = pd.DataFrame(catalogue_data, columns=['Product Name', 'Category', 'Price'])

    assert task_func(mystrings, n_products, seed).equals(catalogue_df)

def test_task_func_with_default_args():
    mystrings = ['Product 1', 'Product 2', 'Product 3']
    n_products = 5
    catalogue_data = []
    for _ in range(n_products):
        product_name = mystrings[randint(0, len(mystrings) - 1)].replace(' ', '_')
        category = CATEGORIES[randint(0, len(CATEGORIES) - 1)]
        price = round(np.random.normal(50, 10), 2)
        catalogue_data.append([product_name, category, price])

    catalogue_df = pd.DataFrame(catalogue_data, columns=['Product Name', 'Category', 'Price'])

    assert task_func(mystrings, n_products).equals(catalogue_df)