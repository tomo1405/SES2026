from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd
import pytz
from src_0051 import task_func


def test_task_func():
    timestamp = 1631833600  # Example timestamp
    df, ax = task_func(timestamp)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape == (len(TIMEZONES), 2)
    assert df.columns.tolist() == ["Timezone", "Datetime"]
    assert df["Timezone"].tolist() == TIMEZONES
    assert df["Datetime"].dt.tz_localize(pytz.UTC).dt.tz_convert(pytz.timezone(TIMEZONES[0])).strftime(DATE_FORMAT).tolist() == [
        datetime.fromtimestamp(timestamp, pytz.timezone(tz)).strftime(DATE_FORMAT)
        for tz in TIMEZONES
    ]
    assert ax.get_xlabel() == "Timezone"
    assert ax.get_ylabel() == "Datetime"
    assert ax.get_title() == "Datetime = f(Timezone)"