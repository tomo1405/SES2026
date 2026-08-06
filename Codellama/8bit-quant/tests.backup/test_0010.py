import pytest
from src_0010 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def test_task_func():
    list_of_pairs = [("A", 10), ("B", 20), ("C", 30)]
    df, ax = task_func(list_of_pairs)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape == (3, 2)
    assert df.columns.tolist() == ["Category", "Value"]
    assert df["Category"].tolist() == ["A", "B", "C"]
    assert df["Value"].tolist() == [10, 20, 30]
    assert ax.get_title() == "Category vs Value"
    assert ax.get_xlabel() == "Category"
    assert ax.get_ylabel() == "Value"
    assert ax.get_xticks() == ["A", "B", "C"]
    assert ax.get_yticks() == [10, 20, 30]