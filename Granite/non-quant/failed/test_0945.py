import pytest
from src_0945 import task_func

def test_task_func():
    # Test case 1: Default arguments
    prices_df, ax = task_func()
    assert isinstance(prices_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert prices_df.shape == (13, 2)
    assert ax.get_title() == 'Stock Prices'
    assert ax.get_xlabel() == 'Date'
    assert ax.get_ylabel() == 'Price'
    assert ax.grid_lines_enabled()

    # Test case 2: Custom arguments
    prices_df, ax = task_func(start_date='2022-01-01', periods=52, freq='WOM-3FRI', seed=42)
    assert isinstance(prices_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert prices_df.shape == (52, 2)
    assert ax.get_title() == 'Stock Prices'
    assert ax.get_xlabel() == 'Date'
    assert ax.get_ylabel() == 'Price'
    assert ax.grid_lines_enabled()