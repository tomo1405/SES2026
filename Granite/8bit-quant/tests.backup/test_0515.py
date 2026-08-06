import pytest
from src_0515 import task_func

def test_task_func():
    array = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
    df, ax = task_func(array)

    # Test if the returned values are of the correct type
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)

    # Test if the DataFrame has the correct columns
    assert list(df.columns) == ["A", "B", "C", "D", "E"]

    # Test if the plot is correct
    assert ax.get_xlabel() == "Index"
    assert ax.get_ylabel() == "Value"
    assert ax.get_title() == "Sums of Columns"