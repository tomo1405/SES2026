import matplotlib.pyplot as plt
import pandas as pd
import pytz
from src_0051 import task_func


def test_task_func():
    timestamp = 1637853200  # Example timestamp
    df, ax = task_func(timestamp)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape == (len(TIMEZONES), 2)
    assert df.columns.tolist() == ["Timezone", "Datetime"]
    assert df["Timezone"].tolist() == TIMEZONES
    assert df["Datetime"].dt.tz.tolist() == [pytz.timezone(tz) for tz in TIMEZONES]
    assert ax.get_xlabel() == "Timezone"
    assert ax.get_ylabel() == "Datetime"
    assert ax.get_title() == "Datetime = f(Timezone)"