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
    assert len(prices_df) == 13
    assert prices_df.index.name == 'Date'
    assert prices_df.columns == ['Price']
    assert ax.get_title() == 'Stock Prices'
    assert ax.get_xlabel() == 'Date'
    assert ax.get_ylabel() == 'Price'
    assert ax.get_autoscale_on() == True
    assert ax.get_xgridlines() == []
    assert ax.get_ygridlines() == []