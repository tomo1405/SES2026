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
    assert df.shape == (3, 2)
    assert ax.get_title() == "Category vs Value"