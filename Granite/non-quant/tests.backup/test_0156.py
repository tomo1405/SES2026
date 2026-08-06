import pandas as pd
import matplotlib.pyplot as plt
import pytest
from src_0156 import task_func

# Constants
COLUMN_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def test_task_func():
    data = [[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16]]
    df, ax = task_func(data)

    # Test if the returned object is a tuple
    assert isinstance(df, tuple) and len(df) == 2
    assert isinstance(ax, plt.Axes)

    # Test if the DataFrame has the expected columns
    assert all(col in df.columns for col in COLUMN_NAMES)

    # Test if the 'Average' column contains the correct values
    assert df['Average'].tolist() == [5, 13]

    # Test if the Y-axis label is set correctly
    assert ax.get_ylabel() == 'Average'