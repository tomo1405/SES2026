import matplotlib
import pandas as pd
import pytest
from src_0087 import task_func


def test_task_func():
    # Test that the function returns a tuple with two elements
    result = task_func()
    assert len(result) == 2

    # Test that the first element is a pandas DataFrame
    df, ax = result
    assert isinstance(df, pd.DataFrame)

    # Test that the DataFrame has the correct columns
    assert list(df.columns) == ["Student", "Score"]

    # Test that the second element is a matplotlib Axes object
    assert isinstance(ax, matplotlib.axes.Axes)

    # Test that the Axes object has the correct ylabel
    assert ax.get_ylabel() == "Score"

    # Test that the DataFrame is sorted by Score
    assert list(df.sort_values("Score").index) == list(df["Score"].sort_values().index)

    # Test that the function raises a ValueError if the students list is empty
    with pytest.raises(ValueError):
        task_func(students=[])