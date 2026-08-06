import pytest
from src_0051 import task_func

def test_task_func():
    timestamp = 1647225600
    df, ax = task_func(timestamp)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert len(df) == len(TIMEZONES)
    assert all(df["Timezone"] == TIMEZONES)
    assert all(df["Datetime"] == [
        datetime.fromtimestamp(timestamp, pytz.timezone(tz)).strftime(DATE_FORMAT)
        for tz in TIMEZONES
    ])
    assert ax.get_xlabel() == "Timezone"
    assert ax.get_ylabel() == "Datetime"
    assert ax.get_title() == "Datetime = f(Timezone)"