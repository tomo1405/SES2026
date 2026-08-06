python
import pytest
from src_0051 import task_func

def test_task_func():
    timestamp = 1622505600
    df, ax = task_func(timestamp)
    assert df.shape == (5, 2)
    assert ax.get_xlabel() == "Timezone"
    assert ax.get_ylabel() == "Datetime"
    assert ax.get_title() == "Datetime = f(Timezone)"