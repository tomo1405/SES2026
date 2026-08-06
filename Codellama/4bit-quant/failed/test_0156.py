import pytest
from src_0156 import task_func

def test_task_func():
    # Test case 1: Test that the function returns a tuple of DataFrame and Axis
    data = [[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16]]
    df, ax = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axis)

    # Test case 2: Test that the DataFrame has the correct column names
    assert list(df.columns) == COLUMN_NAMES

    # Test case 3: Test that the DataFrame has the correct number of rows
    assert len(df) == len(data)

    # Test case 4: Test that the Axis has the correct label
    assert ax.get_ylabel() == 'Average'

    # Test case 5: Test that the Axis has the correct data
    assert ax.get_data() == df['Average'].values