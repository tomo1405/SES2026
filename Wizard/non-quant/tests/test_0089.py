python
import pytest
from src_0089 import task_func

def test_task_func():
    start_date = datetime(2021, 1, 1)
    end_date = datetime(2021, 1, 31)
    df, ax = task_func(start_date, end_date)
    assert df.shape == (31, 2)
    assert ax.get_ylabel() == "Sales"