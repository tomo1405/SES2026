import pytest
from src_0463 import task_func

def test_task_func():
    # Test that the function returns a tuple with two elements
    result = task_func()
    assert len(result) == 2

    # Test that the first element is a pandas DataFrame
    df, ax = result
    assert isinstance(df, pd.DataFrame)

    # Test that the second element is a matplotlib Axes object
    assert isinstance(ax, matplotlib.axes.Axes)

    # Test that the DataFrame has the correct columns
    assert list(df.columns) == ["Category", "Value"]

    # Test that the DataFrame has the correct number of rows
    assert len(df) == 100

    # Test that the Axes object has the correct title
    assert ax.get_title() == "Category Counts"

    # Test that the Axes object has the correct x-axis label
    assert ax.get_xlabel() == "Category"

    # Test that the Axes object has the correct y-axis label
    assert ax.get_ylabel() == "Count"

    # Test that the Axes object has the correct x-axis limits
    assert ax.get_xlim() == (0, 5)

    # Test that the Axes object has the correct y-axis limits
    assert ax.get_ylim() == (0, 100)