import pytest
from src_0503 import task_func

def test_task_func():
    ax, df = task_func()
    assert isinstance(ax, sns.axis.LinePlot)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 7
    assert all(df["Date"] >= datetime.now().date() - timedelta(days=7))
    assert all(df["Activity"].isin(["Running", "Swimming", "Cycling", "Yoga", "Weight Training"]))
    assert all(df["Duration"] >= 0)
    assert all(df["Duration"] <= 120)