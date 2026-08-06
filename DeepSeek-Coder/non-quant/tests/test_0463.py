import pytest
from src_0463 import task_func

def test_task_func():
    result = task_func()
    assert isinstance(result, tuple), "The function should return a tuple."
    df, ax = result
    assert isinstance(df, pd.DataFrame), "The first element of the tuple should be a DataFrame."
    assert isinstance(ax, plt.Axes), "The second element of the tuple should be a matplotlib Axes object."
    assert len(df) == 100, "The DataFrame should have 100 rows."
    assert df["Category"].nunique() <= 5, "The number of unique categories should not exceed 5."