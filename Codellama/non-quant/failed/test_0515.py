import pytest
from src_0515 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    # Test case 1: Test with a valid array
    array = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
    df, ax = task_func(array)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape == (2, 5)
    assert ax.get_title() == "Sums"
    assert ax.get_xlabel() == "Columns"
    assert ax.get_ylabel() == "Sum"

    # Test case 2: Test with an invalid array
    array = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
    with pytest.raises(ValueError):
        task_func(array)

    # Test case 3: Test with a valid array but invalid columns
    array = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
    with pytest.raises(ValueError):
        task_func(array, columns=["A", "B", "C", "D", "E", "F"])

    # Test case 4: Test with a valid array and valid columns
    array = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
    df, ax = task_func(array, columns=["A", "B", "C", "D", "E"])
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape == (2, 5)
    assert ax.get_title() == "Sums"
    assert ax.get_xlabel() == "Columns"
    assert ax.get_ylabel() == "Sum"