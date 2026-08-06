import pandas as pd
import pytest
from src_0050 import task_func


def test_task_func():
    # Test case 1: timestamps is empty
    with pytest.raises(ValueError):
        task_func([])

    # Test case 2: timestamps is not empty
    timestamps = [1641811200, 1641811201, 1641811202]
    df, ax = task_func(timestamps)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, tuple)
    assert len(ax) == 2