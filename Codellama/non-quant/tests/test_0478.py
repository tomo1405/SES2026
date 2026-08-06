import matplotlib.pyplot as plt
import pandas as pd
from src_0478 import task_func


def test_task_func():
    # Test that the function returns a tuple with two elements
    result = task_func()
    assert isinstance(result, tuple)
    assert len(result) == 2

    # Test that the first element of the tuple is a pandas DataFrame
    df, ax = result
    assert isinstance(df, pd.DataFrame)

    # Test that the second element of the tuple is a matplotlib Axes object
    assert isinstance(ax, plt.Axes)

    # Test that the DataFrame has the correct columns
    assert set(df.columns) == {"x", "y", "category"}

    # Test that the DataFrame has the correct number of rows
    assert len(df) == 100

    # Test that the DataFrame has the correct values in the "category" column
    assert set(df["category"].unique()) == {"A", "B", "C", "D", "E"}

    # Test that the Axes object has the correct number of scatter plots
    assert len(ax.get_children()) == 5

    # Test that the scatter plots have the correct labels
    assert ax.get_legend().get_texts()[0].get_text() == "A"
    assert ax.get_legend().get_texts()[1].get_text() == "B"
    assert ax.get_legend().get_texts()[2].get_text() == "C"
    assert ax.get_legend().get_texts()[3].get_text() == "D"
    assert ax.get_legend().get_texts()[4].get_text() == "E"