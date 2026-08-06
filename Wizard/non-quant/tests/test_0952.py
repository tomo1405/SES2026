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

# Test case 1
mystrings = ['apple', 'banana', 'cherry', 'date', 'elderberry']
n_products = 10
seed = 0
expected_df = pd.DataFrame(
    [['apple_1', 'Electronics', 46.34],
     ['banana_2', 'Clothing', 52.16],
     ['cherry_3', 'Home & Kitchen', 49.9],
     ['date_4', 'Books', 48.76],
     ['elderberry_5', 'Toys & Games', 50.12],
     ['apple_6', 'Electronics', 46.34],
     ['banana_7', 'Clothing', 52.16],
     ['cherry_8', 'Home & Kitchen', 49.9],
     ['date_9', 'Books', 48.76],
     ['elderberry_10', 'Toys & Games', 50.12]],
    columns=['Product Name', 'Category', 'Price']
)
result_df = task_func(mystrings, n_products, seed)
assert expected_df.equals(result_df)

# Test case 2
mystrings = ['apple', 'banana', 'cherry', 'date', 'elderberry']
n_products = 5
seed = 1
expected_df = pd.DataFrame(
    [['apple_1', 'Electronics', 46.34],
     ['banana_2', 'Clothing', 52.16],
     ['cherry_3', 'Home & Kitchen', 49.9],
     ['date_4', 'Books', 48.76],
     ['elderberry_5', 'Toys & Games', 50.12]],
    columns=['Product Name', 'Category', 'Price']
)
result_df = task_func(mystrings, n_products, seed)
assert expected_df.equals(result_df)

# Test case 3
mystrings = ['apple', 'banana', 'cherry', 'date', 'elderberry']
n_products = 15
seed = 2
expected_df = pd.DataFrame(
    [['apple_1', 'Electronics', 46.34],
     ['banana_2', 'Clothing', 52.16],
     ['cherry_3', 'Home & Kitchen', 49.9],
     ['date_4', 'Books', 48.76],
     ['elderberry_5', 'Toys & Games', 50.12],
     ['apple_6', 'Electronics', 46.34],
     ['banana_7', 'Clothing', 52.16],
     ['cherry_8', 'Home & Kitchen', 49.9],
     ['date_9', 'Books', 48.76],
     ['elderberry_10', 'Toys & Games', 50.12],
     ['apple_11', 'Electronics', 46.34],
     ['banana_12', 'Clothing', 52.16],
     ['cherry_13', 'Home & Kitchen', 49.9],
     ['date_14', 'Books', 48.76],
     ['elderberry_15', 'Toys & Games', 50.12]],
    columns=['Product Name', 'Category', 'Price']
)
result_df = task_func(mystrings, n_products, seed)
assert expected_df.equals(result_df)