import pytest
from src_0151 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_with_data():
    product_dict = {
        'A': (10, 20),
        'B': (15, 25),
        'C': (20, 30)
    }
    product_keys = ['A', 'B', 'C']

    df, ax = task_func(product_dict, product_keys)

    # Check if DataFrame is not empty
    assert not df.empty

    # Check if DataFrame has the correct columns
    expected_columns = ['Product', 'Quantity', 'Price', 'Profit', 'Average Price', 'Average Profit']
    assert list(df.columns) == expected_columns

    # Check if DataFrame has the correct data
    expected_data = [
        ['A', 10, 20, 200],
        ['B', 15, 25, 375],
        ['C', 20, 30, 600]
    ]
    assert df.to_numpy().tolist() == expected_data

    # Check if average price and profit are calculated correctly
    avg_price = np.mean([20, 25, 30])
    avg_profit = np.mean([200, 375, 600])
    assert df['Average Price'].iloc[0] == avg_price
    assert df['Average Profit'].iloc[0] == avg_profit

    # Check if plot is created
    assert isinstance(ax, plt.AxesSubplot)

def test_task_func_with_empty_data():
    product_dict = {}
    product_keys = []

    df, ax = task_func(product_dict, product_keys)

    # Check if DataFrame is empty
    assert df.empty

    # Check if plot is None
    assert ax is None