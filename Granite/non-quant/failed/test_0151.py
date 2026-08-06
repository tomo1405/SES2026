import pandas as pd
import numpy as np
from src_0151 import task_func

def test_task_func():
    product_dict = {'A': (10, 10), 'B': (20, 20), 'C': (30, 30)}
    product_keys = list(product_dict.keys())
    expected_columns = ['Product', 'Quantity', 'Price', 'Profit', 'Average Price', 'Average Profit']
    expected_data = [
        ['A', 10, 10, 100, None, None],
        ['B', 20, 20, 400, None, None],
        ['C', 30, 30, 900, None, None]
    ]
    expected_df = pd.DataFrame(expected_data, columns=expected_columns)
    expected_ax = None

    df, ax = task_func(product_dict, product_keys)

    assert isinstance(df, pd.DataFrame)
    assert df.columns.tolist() == expected_columns
    assert df.equals(expected_df)
    assert ax is expected_ax

def test_task_func_with_empty_dict():
    product_dict = {}
    product_keys = list(product_dict.keys())
    expected_columns = ['Product', 'Quantity', 'Price', 'Profit', 'Average Price', 'Average Profit']
    expected_data = []
    expected_df = pd.DataFrame(expected_data, columns=expected_columns)
    expected_ax = None

    df, ax = task_func(product_dict, product_keys)

    assert isinstance(df, pd.DataFrame)
    assert df.columns.tolist() == expected_columns
    assert df.equals(expected_df)
    assert ax is expected_ax