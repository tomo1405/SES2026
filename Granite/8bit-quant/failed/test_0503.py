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