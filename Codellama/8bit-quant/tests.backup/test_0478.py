import pytest
from src_0478 import task_func

def test_task_func():
    # Test that the function returns a DataFrame and an Axes object
    df, ax = task_func()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)

    # Test that the DataFrame has the correct columns
    assert set(df.columns) == {"x", "y", "category"}

    # Test that the Axes object has the correct number of scatter plots
    assert len(ax.get_children()) == len(CATEGORIES)

    # Test that the scatter plots have the correct labels
    for i, category in enumerate(CATEGORIES):
        assert ax.get_children()[i].get_label() == category

    # Test that the scatter plots have the correct x and y values
    for i, category in enumerate(CATEGORIES):
        assert ax.get_children()[i].get_xdata() == df[df["category"] == category]["x"]
        assert ax.get_children()[i].get_ydata() == df[df["category"] == category]["y"]