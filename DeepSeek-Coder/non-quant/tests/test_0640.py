import pytest
from src_0640 import task_func

def test_task_func():
    df, _ = task_func()
    assert isinstance(df, pd.DataFrame), "The returned object is not a DataFrame."
    assert not df.empty, "The DataFrame is empty."
    assert len(df.columns) > 0, "The DataFrame has no columns."
    assert len(df.index) > 0, "The DataFrame has no rows."