import pytest
from src_0010 import task_func

def test_task_func():
    list_of_pairs = [("A", 10), ("B", 20), ("C", 30)]
    df, ax = task_func(list_of_pairs)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.columns.tolist() == ["Category", "Value"]
    assert ax.get_title() == "Category vs Value"