import string

import matplotlib.pyplot as plt
import pandas as pd
from src_1034 import task_func


def test_task_func():
    df, ax = task_func()
    
    # Check if df is a DataFrame with the correct shape
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (26**3, 3), f"Expected shape (26^3, 3), but got {df.shape}"
    
    # Check if the columns are correctly named
    assert list(df.columns) == ["a", "b", "c"], "DataFrame columns should be ['a', 'b', 'c']"
    
    # Check if ax is a matplotlib Axes object
    assert isinstance(ax, plt.Axes), "ax should be a matplotlib Axes object"
    
    # Check if the value counts are calculated correctly
    value_counts = df["a"].value_counts().reindex(list(string.ascii_lowercase), fill_value=0)
    assert all(value_counts == 26**2), "Value counts for column 'a' should all be 26^2"

# To run the tests, use the following command in the terminal:
# pytest -v