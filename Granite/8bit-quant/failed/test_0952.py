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
    assert catalogue_df['Product Name'].dtype == np.object
    assert catalogue_df['Category'].dtype == np.object
    assert catalogue_df['Price'].dtype == np.float64
    assert catalogue_df['Product Name'].iloc[0] == 'Product_1'
    assert catalogue_df['Category'].iloc[0] in CATEGORIES
    assert catalogue_df['Price'].iloc[0] >= 50.0 and catalogue_df['Price'].iloc[0] <= 60.0