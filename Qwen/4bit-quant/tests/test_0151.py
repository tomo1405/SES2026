import numpy as np
import pandas as pd
from src_0151 import task_func


def test_task_func_with_data():
    product_dict = {
        'A': (10, 20),
        'B': (15, 25),
        'C': (5, 30)
    }
    product_keys = ['A', 'B', 'C']

    df, ax = task_func(product_dict, product_keys)

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 3
    assert all(column in df.columns for column in ['Product', 'Quantity', 'Price', 'Profit', 'Average Price', 'Average Profit'])

    expected_avg_price = np.mean([20, 25, 30])
    expected_avg_profit = np.mean([200, 375, 150])

    assert df['Average Price'].iloc[0] == expected_avg_price
    assert df['Average Profit'].iloc[0] == expected_avg_profit

    assert ax is not None

def test_task_func_with_empty_data():
    product_dict = {}
    product_keys = []

    df, ax = task_func(product_dict, product_keys)

    assert isinstance(df, pd.DataFrame)
    assert df.empty
    assert ax is None

def test_task_func_with_single_product():
    product_dict = {
        'D': (20, 40)
    }
    product_keys = ['D']

    df, ax = task_func(product_dict, product_keys)

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1
    assert all(column in df.columns for column in ['Product', 'Quantity', 'Price', 'Profit', 'Average Price', 'Average Profit'])

    expected_avg_price = 40
    expected_avg_profit = 800

    assert df['Average Price'].iloc[0] == expected_avg_price
    assert df['Average Profit'].iloc[0] == expected_avg_profit

    assert ax is not None