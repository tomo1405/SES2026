import pandas as pd
from src_0050 import task_func


def test_task_func():
    timestamps = [1630563200, 1630563201, 1630563202]
    df, ax = task_func(timestamps)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, tuple)
    assert len(ax) == 2
    assert isinstance(ax[0], np.ndarray)
    assert isinstance(ax[1], np.ndarray)