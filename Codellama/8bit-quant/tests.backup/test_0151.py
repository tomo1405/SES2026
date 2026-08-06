import pytest
from src_0151 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    product_dict = {'A': (10, 100), 'B': (20, 200), 'C': (30, 300)}
    product_keys = ['A', 'B', 'C']
    df, ax = task_func(product_dict, product_keys)

    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert df.shape == (3, 5)
    assert df.columns.tolist() == ['Product', 'Quantity', 'Price', 'Profit', 'Average Price', 'Average Profit']
    assert np.allclose(df['Average Price'], 200)
    assert np.allclose(df['Average Profit'], 2000)