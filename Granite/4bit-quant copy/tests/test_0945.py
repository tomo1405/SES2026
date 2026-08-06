import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pytest

def task_func(start_date='2016-01-01', periods=13, freq='WOM-2FRI', seed=0):
    if seed is not None:
        np.random.seed(seed)
    date_range = pd.date_range(start=start_date, periods=periods, freq=freq)
    stock_prices = np.random.uniform(low=100, high=500, size=periods)

    prices_df = pd.DataFrame({'Date': date_range, 'Price': stock_prices})
    prices_df.set_index('Date', inplace=True)

    fig, ax = plt.subplots(figsize=(10, 6))
    # ax.plot(prices_df.index, prices_df['Price'], marker='o')
    prices_df.plot(ax=ax, marker='o')
    pd.plotting.register_matplotlib_converters()
    ax.set_title('Stock Prices')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.grid(True)
    
    return prices_df, ax

def test_task_func():
    # Test case 1: Default parameters
    prices_df, ax = task_func()
    assert isinstance(prices_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert prices_df.shape == (13, 2)
    assert ax.get_title() == 'Stock Prices'
    assert ax.get_xlabel() == 'Date'
    assert ax.get_ylabel() == 'Price'
    assert ax.get_legend() is None

    # Test case 2: Custom parameters
    prices_df, ax = task_func(start_date='2020-01-01', periods=5, freq='D', seed=1)
    assert isinstance(prices_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert prices_df.shape == (5, 2)
    assert ax.get_title() == 'Stock Prices'
    assert ax.get_xlabel() == 'Date'
    assert ax.get_ylabel() == 'Price'
    assert ax.get_legend() is None

if __name__ == '__main__':
    pytest.main()