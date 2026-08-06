import pytest
from src_0487 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    start_time = 1640995200000
    end_time = 1640995200000 + 1000
    step = 100
    trend = 1
    seed = 42

    ax = task_func(start_time, end_time, step, trend, seed)

    assert isinstance(ax, pd.DataFrame)
    assert ax.shape == (10, 2)
    assert ax.columns.tolist() == ["Time", "Value"]
    assert ax.dtypes.tolist() == [np.datetime64, np.float64]
    assert ax.iloc[0, 0] == datetime.fromtimestamp(start_time / 1000).strftime("%Y-%m-%d %H:%M:%S.%f")
    assert ax.iloc[0, 1] == np.random.normal(size=1) + trend * 0
    assert ax.iloc[-1, 0] == datetime.fromtimestamp(end_time / 1000).strftime("%Y-%m-%d %H:%M:%S.%f")
    assert ax.iloc[-1, 1] == np.random.normal(size=1) + trend * 9