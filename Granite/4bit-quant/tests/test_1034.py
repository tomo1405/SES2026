import string

import matplotlib
import pandas as pd
from src_1034 import task_func


def test_task_func():
    df, ax = task_func()

    # Test that the returned objects are of the correct type
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)

    # Test that the correct number of rows and columns are returned
    assert df.shape == (52, 3)

    # Test that the correct order of letters is returned
    assert df["a"].unique().tolist() == list(string.ascii_lowercase)

    # Test that the correct histogram is returned
    assert ax.get_xlabel() == "a"
    assert ax.get_ylabel() == "Frequency"