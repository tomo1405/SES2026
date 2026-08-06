import matplotlib
import pandas as pd
from src_0087 import task_func


def test_task_func():
    # Test that the function returns a tuple with two elements
    result = task_func()
    assert isinstance(result, tuple)
    assert len(result) == 2

    # Test that the first element of the tuple is a pandas DataFrame
    df, ax = result
    assert isinstance(df, pd.DataFrame)

    # Test that the DataFrame has the correct columns
    assert list(df.columns) == ["Student", "Score"]

    # Test that the DataFrame has the correct number of rows
    assert len(df) == 5

    # Test that the second element of the tuple is a matplotlib Axes object
    assert isinstance(ax, matplotlib.axes.Axes)

    # Test that the Axes object has the correct ylabel
    assert ax.get_ylabel() == "Score"

    # Test that the Axes object has the correct xlabel
    assert ax.get_xlabel() == "Student"

    # Test that the Axes object has the correct title
    assert ax.get_title() == "Scores"

    # Test that the Axes object has the correct legend
    assert ax.get_legend() == False

    # Test that the Axes object has the correct x-axis ticks
    assert ax.get_xticks() == ["Alice", "Bob", "Charlie", "David", "Eve"]

    # Test that the Axes object has the correct y-axis ticks
    assert ax.get_yticks() == [0, 20, 40, 60, 80, 100]

    # Test that the Axes object has the correct bar colors
    assert ax.get_bar_colors() == ["blue", "blue", "blue", "blue", "blue"]