python
import pytest
from src_0372 import task_func

def test_task_func():
    l = [1, 2, 3, 4, 5]
    df = task_func(l)
    assert df.shape == (5, 1)
    assert df.iloc[0, 0] == 0.0
    assert df.iloc[1, 0] == 0.25
    assert df.iloc[2, 0] == 0.5
    assert df.iloc[3, 0] == 0.75
    assert df.iloc[4, 0] == 1.0