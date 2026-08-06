import pytest
from src_0503 import task_func

def test_task_func():
    # Test that the function returns a tuple with two elements
    result = task_func()
    assert isinstance(result, tuple)
    assert len(result) == 2

    # Test that the first element of the tuple is a matplotlib.axes.Axes object
    ax, df = result
    assert isinstance(ax, matplotlib.axes.Axes)

    # Test that the second element of the tuple is a pandas.DataFrame object
    assert isinstance(df, pandas.DataFrame)

    # Test that the DataFrame has the correct columns
    assert set(df.columns) == {"Date", "Activity", "Duration"}

    # Test that the DataFrame has the correct data types
    assert df["Date"].dtype == "datetime64[ns]"
    assert df["Activity"].dtype == "object"
    assert df["Duration"].dtype == "int64"

    # Test that the DataFrame has the correct data values
    assert set(df["Activity"].unique()) == {"Running", "Swimming", "Cycling", "Yoga", "Weight Training"}
    assert df["Duration"].min() >= 0
    assert df["Duration"].max() <= 120

    # Test that the line plot has the correct x-axis label
    assert ax.get_xlabel() == "Date"

    # Test that the line plot has the correct y-axis label
    assert ax.get_ylabel() == "Duration"

    # Test that the line plot has the correct title
    assert ax.get_title() == "Activity Duration Over Time"

    # Test that the line plot has the correct legend
    assert ax.get_legend() == "Activity"

    # Test that the line plot has the correct color scheme
    assert ax.get_color_scheme() == "seaborn"