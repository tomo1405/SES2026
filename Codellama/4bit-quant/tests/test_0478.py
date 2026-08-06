import matplotlib.pyplot as plt
import pandas as pd
from src_0478 import task_func


def test_task_func():
    # Test that the function returns a DataFrame and an Axes object
    df, ax = task_func()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)

    # Test that the DataFrame has the correct columns
    assert "x" in df.columns
    assert "y" in df.columns
    assert "category" in df.columns

    # Test that the Axes object has the correct number of scatter plots
    assert len(ax.get_children()) == len(CATEGORIES)

    # Test that the scatter plots have the correct labels
    for category in CATEGORIES:
        assert category in ax.get_legend().get_texts()

    # Test that the scatter plots have the correct colors
    for category in CATEGORIES:
        assert category in ax.get_legend().get_texts()

    # Test that the DataFrame has the correct number of rows
    assert len(df) == N

    # Test that the DataFrame has the correct number of categories
    assert len(df["category"].unique()) == len(CATEGORIES)

    # Test that the DataFrame has the correct category values
    for category in CATEGORIES:
        assert category in df["category"].unique()