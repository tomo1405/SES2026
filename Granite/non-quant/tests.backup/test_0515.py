import pytest
from src_0515 import task_func

@pytest.mark.parametrize("array", [
    [[1, 2, 3, 4, 5]],
    [[10, 20, 30, 40, 50]],
    [[-1, -2, -3, -4, -5]]
])
def test_task_func(array):
    df, ax = task_func(array)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert list(df.columns) == ["A", "B", "C", "D", "E"]
    assert list(df.sum()) == [6, 120, -6]