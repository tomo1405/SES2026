import matplotlib
import pandas
from src_0503 import task_func


def test_task_func():
    # Test that the function returns a tuple with two elements
    result = task_func()
    assert len(result) == 2

    # Test that the first element is a matplotlib.axes.Axes object
    ax, df = result
    assert isinstance(ax, matplotlib.axes.Axes)

    # Test that the second element is a pandas.DataFrame object
    assert isinstance(df, pandas.DataFrame)

    # Test that the DataFrame has the correct columns
    assert list(df.columns) == ["Date", "Activity", "Duration"]

    # Test that the DataFrame has the correct number of rows
    assert len(df) == 7

    # Test that the DataFrame contains the correct data
    expected_data = [
        ["2022-03-05", "Running", 30],
        ["2022-03-05", "Swimming", 45],
        ["2022-03-05", "Cycling", 60],
        ["2022-03-05", "Yoga", 75],
        ["2022-03-05", "Weight Training", 90],
        ["2022-03-06", "Running", 30],
        ["2022-03-06", "Swimming", 45],
        ["2022-03-06", "Cycling", 60],
        ["2022-03-06", "Yoga", 75],
        ["2022-03-06", "Weight Training", 90],
    ]
    assert list(df.values) == expected_data

    # Test that the plot has the correct title
    assert ax.get_title() == "Activity Duration"

    # Test that the plot has the correct x-axis label
    assert ax.get_xlabel() == "Date"

    # Test that the plot has the correct y-axis label
    assert ax.get_ylabel() == "Duration"

    # Test that the plot has the correct legend
    assert ax.get_legend().get_title().get_text() == "Activity"

    # Test that the plot has the correct number of lines
    assert len(ax.get_lines()) == 5

    # Test that the plot has the correct number of points
    assert len(ax.get_points()) == 10