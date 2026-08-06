import pytest
from src_0067 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    # Test with a simple dataset
    data = [
        [1, 2, 3],
        [1, 2, 4],
        [1, 3, 5],
        [2, 2, 6],
        [2, 3, 7]
    ]
    expected_columns = ['col1', 'col2', 'col3', 'col3_nunique']
    expected_data = [
        [1, 2, 3, 2],
        [1, 3, 5, 1],
        [2, 2, 6, 1],
        [2, 3, 7, 1]
    ]

    result_df, ax = task_func(data)

    # Check if the returned DataFrame has the correct structure and data
    assert list(result_df.columns) == expected_columns
    assert result_df.to_dict('records') == expected_data

    # Check if the plot is created
    assert isinstance(ax, plt.Axes)

    # Close the plot to avoid it showing up during testing
    plt.close(ax.figure)