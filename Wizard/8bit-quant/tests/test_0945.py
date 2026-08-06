python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pytest

from src_0945 import task_func

def test_task_func():
    prices_df, ax = task_func()
    assert isinstance(prices_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert prices_df.shape == (13, 2)
    assert prices_df.index[0] == pd.to_datetime('2016-01-01')
    assert prices_df.index[-1] == pd.to_datetime('2016-01-13')
    assert prices_df['Price'].min() >= 100
    assert prices_df['Price'].max() <= 500
    assert ax.get_title() == 'Stock Prices'
    assert ax.get_xlabel() == 'Date'
    assert ax.get_ylabel() == 'Price'
    assert ax.get_xlim() == (pd.to_datetime('2016-01-01'), pd.to_datetime('2016-01-13'))
    assert ax.get_ylim() == (prices_df['Price'].min(), prices_df['Price'].max())
    assert ax.get_gridlines()