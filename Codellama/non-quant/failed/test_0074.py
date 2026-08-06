import pytest
from src_0074 import task_func

def test_task_func():
    db_file = "test_db.db"
    df, ax = task_func(db_file)

    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape[0] > 0
    assert df.shape[1] == 4
    assert ax.shape[0] == 3
    assert ax.shape[1] == 1