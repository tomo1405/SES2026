import pytest
from src_0945 import task_func

def test_task_func():
    # Test that the function returns a tuple with two elements
    result = task_func()
    assert len(result) == 2

    # Test that the first element is a DataFrame with the correct columns
    prices_df, ax = result
    assert isinstance(prices_df, pd.DataFrame)
    assert 'Date' in prices_df.columns
    assert 'Price' in prices_df.columns

    # Test that the second element is a matplotlib Axes object
    assert isinstance(ax, plt.Axes)

    # Test that the DataFrame has the correct index and columns
    assert prices_df.index.name == 'Date'
    assert prices_df['Price'].dtype == np.float64

    # Test that the Axes object has the correct title, xlabel, and ylabel
    assert ax.get_title() == 'Stock Prices'
    assert ax.get_xlabel() == 'Date'
    assert ax.get_ylabel() == 'Price'

    # Test that the Axes object has a grid
    assert ax.grid(True)

    # Test that the DataFrame has the correct number of rows
    assert len(prices_df) == 13

    # Test that the DataFrame has the correct number of columns
    assert len(prices_df.columns) == 2

    # Test that the DataFrame has the correct index values
    assert prices_df.index.values.tolist() == [
        '2016-01-01', '2016-01-08', '2016-01-15', '2016-01-22', '2016-01-29',
        '2016-02-05', '2016-02-12', '2016-02-19', '2016-02-26', '2016-03-04',
        '2016-03-11', '2016-03-18', '2016-03-25'
    ]

    # Test that the DataFrame has the correct column values
    assert prices_df['Price'].values.tolist() == [
        100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100
    ]