import matplotlib.pyplot as plt
import pandas as pd
from src_0156 import task_func


def test_task_func():
    # Test case 1: Test that the function returns a tuple with a DataFrame and an Axes object
    data = [[1, 2, 3, 4, 5, 6, 7, 8], [2, 4, 6, 8, 10, 12, 14, 16]]
    df, ax = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)

    # Test case 2: Test that the DataFrame has the correct column names
    assert list(df.columns) == COLUMN_NAMES

    # Test case 3: Test that the DataFrame has the correct number of rows
    assert len(df) == len(data)

    # Test case 4: Test that the Axes object has the correct y-axis label
    assert ax.get_ylabel() == 'Average'

    # Test case 5: Test that the Axes object has the correct x-axis label
    assert ax.get_xlabel() == 'Index'

    # Test case 6: Test that the Axes object has the correct title
    assert ax.get_title() == 'Average'

    # Test case 7: Test that the Axes object has the correct legend
    assert ax.get_legend() == 'Average'

    # Test case 8: Test that the Axes object has the correct grid
    assert ax.get_grid() == True

    # Test case 9: Test that the Axes object has the correct x-axis limits
    assert ax.get_xlim() == (0, len(data))

    # Test case 10: Test that the Axes object has the correct y-axis limits
    assert ax.get_ylim() == (0, 16)