python
import pandas as pd
import numpy as np
import random
from random import randint, seed

# Constants
CATEGORIES = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Toys & Games']

def task_func(mystrings, n_products, seed=0):
    catalogue_data = []
    random.seed(seed)
    np.random.seed(seed)
    for _ in range(n_products):
        product_name = mystrings[randint(0, len(mystrings) - 1)].replace(' ', '_')
        category = CATEGORIES[randint(0, len(CATEGORIES) - 1)]
        price = round(np.random.normal(50, 10), 2)
        catalogue_data.append([product_name, category, price])

    catalogue_df = pd.DataFrame(catalogue_data, columns=['Product Name', 'Category', 'Price'])

    return catalogue_df

# Test the function
def test_task_func():
    # Test case 1
    mystrings = ['apple', 'banana', 'cherry', 'orange']
    n_products = 10
    seed = 0
    expected_df = pd.DataFrame(
        [['apple_1', 'Electronics', 46.34],
         ['banana_2', 'Clothing', 52.16],
         ['cherry_3', 'Home & Kitchen', 49.9],
         ['orange_4', 'Books', 48.76],
         ['apple_5', 'Electronics', 46.34],
         ['banana_6', 'Clothing', 52.16],
         ['cherry_7', 'Home & Kitchen', 49.9],
         ['orange_8', 'Books', 48.76],
         ['apple_9', 'Electronics', 46.34],
         ['banana_10', 'Clothing', 52.16]],
        columns=['Product Name', 'Category', 'Price']
    )
    actual_df = task_func(mystrings, n_products, seed)
    assert actual_df.equals(expected_df)

    # Test case 2
    mystrings = ['apple', 'banana', 'cherry', 'orange']
    n_products = 5
    seed = 1
    expected_df = pd.DataFrame(
        [['cherry_1', 'Home & Kitchen', 49.9],
         ['orange_2', 'Books', 48.76],
         ['apple_3', 'Electronics', 46.34],
         ['banana_4', 'Clothing', 52.16],
         ['cherry_5', 'Home & Kitchen', 49.9]],
        columns=['Product Name', 'Category', 'Price']
    )
    actual_df = task_func(mystrings, n_products, seed)
    assert actual_df.equals(expected_df)

test_task_func()