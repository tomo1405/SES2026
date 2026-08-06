import pandas as pd
import numpy as np
from src_0151 import task_func

def test_task_func():
    product_dict = {'A': (10, 10), 'B': (5, 20), 'C': (8, 15)}
    product_keys = list(product_dict.keys())
    df, ax = task_func(product_dict, product_keys)

    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, object) or ax is None
    if df is not None:
        assert 'Product' in df.columns
        assert 'Quantity' in df.columns
        assert 'Price' in df.columns
        assert 'Profit' in df.columns
        assert 'Average Price' in df.columns
        assert 'Average Profit' in df.columns
        assert df.shape == (len(product_dict), 5)

product_dict_empty = {}
product_keys_empty = []
df_empty, ax_empty = task_func(product_dict_empty, product_keys_empty)

assert isinstance(df_empty, pd.DataFrame)
assert isinstance(ax_empty, object) or ax_empty is None
if df_empty is not None:
    assert df_empty.empty