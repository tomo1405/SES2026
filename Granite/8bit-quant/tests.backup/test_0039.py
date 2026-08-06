import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from src_0039 import task_func
import pytest

def test_task_func():
    data_matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
    df, ax = task_func(data_matrix)
    assert isinstance(df, pd.DataFrame)
    assert "Mean" in df.columns
    assert isinstance(ax, plt.Axes)

def test_task_func_with_invalid_input():
    with pytest.raises(ValueError):
        task_func("invalid input")