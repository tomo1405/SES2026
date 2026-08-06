python
import pandas as pd
import numpy as np
import pytest

def task_func(file_path="data.csv", columns=["A", "B", "C"]):
    df = pd.read_csv(file_path, dtype=float)
    ax = df[columns].plot()
    croot = np.cbrt(df[columns])
    return df, ax, croot

def test_task_func():
    df, ax, croot = task_func()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes._subplots.AxesSubplot)
    assert isinstance(croot, pd.DataFrame)
    assert croot.shape == (3, 1)