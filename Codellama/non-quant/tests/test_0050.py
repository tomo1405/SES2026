import matplotlib.pyplot as plt
import pandas as pd
import pytest
from src_0050 import task_func


def test_task_func_empty_input():
    with pytest.raises(ValueError):
        task_func([])

def test_task_func_valid_input():
    timestamps = [1640995200, 1640995201, 1640995202]
    df, ax = task_func(timestamps)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert len(df) == 3
    assert len(ax.patches) == 3