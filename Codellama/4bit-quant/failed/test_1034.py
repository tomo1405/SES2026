import pytest
from src_1034 import task_func

def test_task_func():
    df, ax = task_func()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert len(df) == 26
    assert len(df.columns) == 3
    assert df.columns.tolist() == ["a", "b", "c"]
    assert all(df["a"].isin(string.ascii_lowercase))
    assert all(df["b"].isin(string.ascii_lowercase))
    assert all(df["c"].isin(string.ascii_lowercase))
    assert all(df["a"].value_counts().index.isin(string.ascii_lowercase))
    assert all(df["b"].value_counts().index.isin(string.ascii_lowercase))
    assert all(df["c"].value_counts().index.isin(string.ascii_lowercase))
    assert ax.get_xlabel() == "a"
    assert ax.get_ylabel() == "Count"
    assert ax.get_title() == "Value Counts"
    assert ax.get_xticks() == string.ascii_lowercase
    assert ax.get_yticks() == range(0, 27)
    assert ax.get_xticklabels() == string.ascii_lowercase
    assert ax.get_yticklabels() == range(0, 27)