import pandas as pd
import pytest
from src_0503 import task_func


def test_task_func():
    ax, df = task_func()
    assert ax is not None
    assert df is not None
    assert isinstance(df, pd.DataFrame)
    assert "Date" in df.columns
    assert "Activity" in df.columns
    assert "Duration" in df.columns

def test_task_func_days_in_past():
    with pytest.raises(ValueError):
        task_func(days_in_past=0)

def test_task_func_random_seed():
    ax1, df1 = task_func(random_seed=0)
    ax2, df2 = task_func(random_seed=0)
    assert df1.equals(df2)
    assert ax1.get_lines()[0].get_ydata() == ax2.get_lines()[0].get_ydata()