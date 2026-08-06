import matplotlib
import pandas as pd
import pytest
from src_0539 import task_func


def test_task_func():
    # Test that the function raises a ValueError when the table has less than 2 numerical columns
    with pytest.raises(ValueError):
        task_func("test.db", "test_table")

    # Test that the function returns a valid plot when the table has at least 2 numerical columns
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    ax = task_func("test.db", "test_table")
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_xlabel() == "A"
    assert ax.get_ylabel() == "B"