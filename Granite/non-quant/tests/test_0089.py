from datetime import datetime

import matplotlib
import pandas as pd
from src_0089 import task_func


def test_task_func():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 31)
    seed = 42
    df, ax = task_func(start_date, end_date, seed)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert df.shape == (31, 2)
    assert df["Date"].iloc[0] == start_date
    assert df["Date"].iloc[-1] == end_date
    assert df["Sales"].min() >= 0
    assert df["Sales"].max() <= 500