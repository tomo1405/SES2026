import pytest
from src_0151 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    # Test with non-empty product_dict and product_keys
    product_dict = {
        'A': (10, 20),
        'B': (15, 30),
        'C': (20, 40)
    }
    product_keys = ['A', 'B', 'C']
    df, ax = task_func(product_dict, product_keys)
    
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert list(df.columns) == ['Product', 'Quantity', 'Price', 'Profit', 'Average Price', 'Average Profit']
    
    expected_data = [
        ['A', 10, 20, 200],
        ['B', 15, 30, 450],
        ['C', 20, 40, 800]
    ]
    assert df.to_numpy().tolist() == expected_data
    
    avg_price = np.mean([20, 30, 40])
    avg_profit = np.mean([200, 450, 800])
    assert df['Average Price'].iloc[0] == avg_price
    assert df['Average Profit'].iloc[0] == avg_profit
    assert ax is not None

    # Test with empty product_dict and product_keys
    product_dict = {}
    product_keys = []
    df, ax = task_func(product_dict, product_keys)
    
    assert isinstance(df, pd.DataFrame)
    assert df.empty
    assert ax is None

    # Test with some keys missing in product_dict
    product_dict = {
        'A': (10, 20),
        'B': (15, 30)
    }
    product_keys = ['A', 'B', 'C']
    df, ax = task_func(product_dict, product_keys)
    
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert list(df.columns) == ['Product', 'Quantity', 'Price', 'Profit', 'Average Price', 'Average Profit']
    
    expected_data = [
        ['A', 10, 20, 200],
        ['B', 15, 30, 450]
    ]
    assert df.to_numpy().tolist() == expected_data
    
    avg_price = np.mean([20, 30])
    avg_profit = np.mean([200, 450])
    assert df['Average Price'].iloc[0] == avg_price
    assert df['Average Profit'].iloc[0] == avg_profit
    assert ax is not None