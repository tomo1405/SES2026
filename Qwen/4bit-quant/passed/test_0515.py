import pytest
from src_0515 import task_func
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    # Test with a simple 2x5 array
    array = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
    df, ax = task_func(array)

    # Check if the DataFrame is created correctly
    expected_df = pd.DataFrame(array, columns=["A", "B", "C", "D", "E"])
    pd.testing.assert_frame_equal(df, expected_df)

    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 5  # There should be one bar for each column

    # Check if the sums are calculated correctly
    expected_sums = pd.Series([7, 9, 11, 13, 15], index=["A", "B", "C", "D", "E"])
    pd.testing.assert_series_equal(df.sum(), expected_sums)

# To run the tests, use the command: pytest <filename>.py