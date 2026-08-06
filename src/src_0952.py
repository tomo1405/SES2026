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