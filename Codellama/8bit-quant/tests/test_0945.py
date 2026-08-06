import pandas as pd
from src_0945 import task_func


def test_task_func():
    # Test that the function returns a tuple with two elements
    result = task_func()
    assert isinstance(result, tuple)
    assert len(result) == 2

    # Test that the first element of the tuple is a pandas DataFrame
    prices_df, ax = result
    assert isinstance(prices_df, pd.DataFrame)

    # Test that the DataFrame has the correct columns
    assert set(prices_df.columns) == {'Date', 'Price'}

    # Test that the DataFrame has the correct index
    assert isinstance(prices_df.index, pd.DatetimeIndex)

    # Test that the second element of the tuple is a matplotlib Axes object
    assert isinstance(ax, plt.Axes)

    # Test that the Axes object has the correct title, xlabel, and ylabel
    assert ax.get_title() == 'Stock Prices'
    assert ax.get_xlabel() == 'Date'
    assert ax.get_ylabel() == 'Price'

    # Test that the Axes object has a grid
    assert ax.get_grid()

    # Test that the DataFrame and Axes object are plotted correctly
    assert prices_df.plot(ax=ax, marker='o')