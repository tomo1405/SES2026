import pytest
from src_0515 import task_func
import pandas as pd
import matplotlib.pyplot as plt

@pytest.fixture
def input_array():
    return [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

def test_task_func(input_array):
    df, ax = task_func(input_array)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert list(df.columns) == ["A", "B", "C", "D", "E"]
    assert df.sum().equals(pd.Series([55, 60, 65, 70, 75]))