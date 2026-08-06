import pytest
from src_0945 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_default_parameters():
    prices_df, ax = task_func()
    assert isinstance(prices_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert len(prices_df) == 13
    assert 'Price' in prices_df.columns
    assert 'Date' not in prices_df.columns  # because Date is set as index

def test_task_func_custom_parameters():
    start_date = '2020-01-01'
    periods = 20
    freq = 'D'
    seed = 42
    prices_df, ax = task_func(start_date=start_date, periods=periods, freq=freq, seed=seed)
    assert isinstance(prices_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert len(prices_df) == 20
    assert 'Price' in prices_df.columns
    assert 'Date' not in prices_df.columns  # because Date is set as index
    assert prices_df.index[0] == pd.to_datetime(start_date)
    assert prices_df.index[-1] == pd.to_datetime(start_date) + pd.Timedelta(days=periods-1)

def test_task_func_seed_reproducibility():
    seed = 123
    _, ax1 = task_func(seed=seed)
    _, ax2 = task_func(seed=seed)
    assert ax1.get_lines()[0].get_ydata() == ax2.get_lines()[0].get_ydata()

def test_task_func_no_seed():
    _, ax1 = task_func(seed=None)
    _, ax2 = task_func(seed=None)
    assert ax1.get_lines()[0].get_ydata() != ax2.get_lines()[0].get_ydata()