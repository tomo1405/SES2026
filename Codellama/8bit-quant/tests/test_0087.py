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

    # Test that the Axes object has the correct y-label
    assert ax.get_ylabel() == "Score"