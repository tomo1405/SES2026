import pytest
from src_0051 import task_func

@pytest.mark.parametrize("timestamp", [1647225600, 1647225600.123456789])
def test_task_func_returns_dataframe(timestamp):
    df, ax = task_func(timestamp)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)

@pytest.mark.parametrize("timestamp", [1647225600, 1647225600.123456789])
def test_task_func_returns_correct_datetimes(timestamp):
    df, ax = task_func(timestamp)
    expected_datetimes = [
        datetime.fromtimestamp(timestamp, pytz.timezone(tz)).strftime(DATE_FORMAT)
        for tz in TIMEZONES
    ]
    assert df["Datetime"].tolist() == expected_datetimes

@pytest.mark.parametrize("timestamp", [1647225600, 1647225600.123456789])
def test_task_func_returns_correct_timezones(timestamp):
    df, ax = task_func(timestamp)
    assert df["Timezone"].tolist() == TIMEZONES

@pytest.mark.parametrize("timestamp", [1647225600, 1647225600.123456789])
def test_task_func_returns_correct_plot(timestamp):
    df, ax = task_func(timestamp)
    assert ax.get_xlabel() == "Timezone"
    assert ax.get_ylabel() == "Datetime"
    assert ax.get_title() == "Datetime = f(Timezone)"