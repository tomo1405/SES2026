python
import pytest
from src_0050 import task_func

def test_task_func():
    timestamps = [1622505600, 1622592000, 1622678400]
    df, ax = task_func(timestamps)
    assert df.shape == (3, 2)
    assert ax.shape == (1, 2)
    assert df.iloc[0]["Timestamp"] == timestamps[0]
    assert df.iloc[1]["Timestamp"] == timestamps[1]
    assert df.iloc[2]["Timestamp"] == timestamps[2]
    assert df.iloc[0]["Datetime"] == "2021-06-01 00:00:00"
    assert df.iloc[1]["Datetime"] == "2021-06-02 00:00:00"
    assert df.iloc[2]["Datetime"] == "2021-06-03 00:00:00"