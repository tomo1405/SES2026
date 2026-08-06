import pytest
from src_1034 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    df, ax = task_func()
    
    # Check if df is a DataFrame
    assert isinstance(df, pd.DataFrame), "The returned object is not a DataFrame"
    
    # Check if df has the correct columns
    assert list(df.columns) == ["a", "b", "c"], "DataFrame does not have the correct columns"
    
    # Check if df has 26^3 rows (since we have all combinations of 3 lowercase letters)
    assert len(df) == 26**3, "DataFrame does not have the expected number of rows"
    
    # Check if ax is a matplotlib Axes object
    assert isinstance(ax, plt.Axes), "The returned object is not a matplotlib Axes object"
    
    # Check if the value counts for column 'a' are correct
    expected_value_counts = pd.Series([26**2] * 26, index=list(string.ascii_lowercase))
    actual_value_counts = df["a"].value_counts().reindex(list(string.ascii_lowercase), fill_value=0)
    pd.testing.assert_series_equal(actual_value_counts, expected_value_counts)