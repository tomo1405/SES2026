python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pytest

def task_func(list_of_pairs):
    df = pd.DataFrame(list_of_pairs, columns=["Category", "Value"])
    plt.figure(figsize=(10, 5))
    sns.barplot(x="Category", y="Value", data=df)
    plt.title("Category vs Value")
    ax = plt.gca()
    return df, ax

def test_task_func():
    list_of_pairs = [("A", 10), ("B", 20), ("C", 30)]
    df, ax = task_func(list_of_pairs)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Category vs Value"
    assert ax.get_xlabel() == "Category"
    assert ax.get_ylabel() == "Value"
    assert ax.get_xlim() == (0, 3)
    assert ax.get_ylim() == (0, 30)
    assert ax.get_xticks() == [0, 1, 2, 3]
    assert ax.get_yticks() == [0, 10, 20, 30]
    assert ax.get_xticklabels() == ["A", "B", "C", ""]
    assert ax.get_yticklabels() == ["0", "10", "20", "30"]