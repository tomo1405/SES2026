import pytest
from src_0089 import task_func

def test_task_func():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 7)
    seed = 42
    df, ax = task_func(start_date, end_date, seed)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape == (7, 2)
    assert df["Date"].dt.date.tolist() == [date.date() for date in pd.date_range(start_date, end_date)]
    assert df["Sales"].dtype == np.int64
    assert ax.get_ylabel() == "Sales"