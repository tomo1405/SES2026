import pytest
from src_0478 import task_func

@pytest.mark.parametrize("N, seed", [(100, 42), (50, 123), (200, 456)])
def test_task_func(N, seed):
    df, ax = task_func(N, seed=seed)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert len(df) == N
    assert len(df["category"].unique()) <= len(task_func.CATEGORIES)
    assert ax.get_legend_handles_labels()[1] == task_func.CATEGORIES