from datetime import datetime

import matplotlib
import numpy as np
import pandas as pd
from src_0089 import task_func


def test_task_func():
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2022, 1, 31)
    seed = 42

    df, ax = task_func(start_date, end_date, seed)

    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert df.shape == (31, 2)
    assert df.columns.tolist() == ["Date", "Sales"]
    assert np.all(df["Date"] == pd.date_range(start_date, end_date))
    assert np.all(df["Sales"] >= 0)
    assert np.all(df["Sales"] <= 500)
    assert ax.get_ylabel() == "Sales"