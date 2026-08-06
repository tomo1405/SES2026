import pytest
from src_0943 import task_func

def test_task_func():
    # Test that the function returns a tuple with two elements
    result = task_func()
    assert isinstance(result, tuple)
    assert len(result) == 2

    # Test that the first element of the tuple is a pandas DataFrame
    sales_df, ax = result
    assert isinstance(sales_df, pd.DataFrame)

    # Test that the second element of the tuple is a matplotlib Axes object
    assert isinstance(ax, plt.Axes)

    # Test that the DataFrame has the correct columns
    assert set(sales_df.columns) == {'Date', 'Category', 'Sales'}

    # Test that the DataFrame has the correct number of rows
    assert len(sales_df) == 13

    # Test that the Axes object has the correct title
    assert ax.get_title() == 'Category-wise Sales Trends'

    # Test that the Axes object has a grid
    assert ax.get_grid()