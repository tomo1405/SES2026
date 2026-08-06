python
import pandas as pd
import matplotlib.pyplot as plt
import pytest

# Constants
COLUMN_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def task_func(data):
    df = pd.DataFrame(data, columns=COLUMN_NAMES)
    df['Average'] = df.mean(axis=1)

    # Creating a new figure and axis for plotting
    fig, ax = plt.subplots()
    df['Average'].plot(ax=ax)
    ax.set_ylabel('Average')  # Setting the Y-axis label to 'Average'

    return df, ax

def test_task_func():
    # Test case 1
    data = [[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16]]
    expected_df = pd.DataFrame(data, columns=COLUMN_NAMES)
    expected_df['Average'] = expected_df.mean(axis=1)
    expected_ax = expected_df['Average'].plot()
    expected_ax.set_ylabel('Average')

    df, ax = task_func(data)

    assert df.equals(expected_df)
    assert ax.equals(expected_ax)

    # Test case 2
    data = [[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16]]
    expected_df = pd.DataFrame(data, columns=COLUMN_NAMES)
    expected_df['Average'] = expected_df.mean(axis=1)
    expected_ax = expected_df['Average'].plot()
    expected_ax.set_ylabel('Average')

    df, ax = task_func(data)

    assert df.equals(expected_df)
    assert ax.equals(expected_ax)