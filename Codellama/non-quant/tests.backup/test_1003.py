import pytest
from src_1003 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    data = [1, 2, 3, 4, 5]
    column_name = "target_column"
    df, ax = task_func(data, column_name)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert column_name in df.columns
    assert pd.api.types.is_numeric_dtype(df[column_name])
    assert df[column_name].hist(ax=ax)
    assert ax.get_title() == f"Histogram of {column_name}"
    assert ax.get_xlabel() == column_name