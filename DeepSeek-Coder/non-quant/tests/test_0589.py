import pytest
from src_0589 import task_func

def test_task_func():
    df = task_func()
    assert isinstance(df, pd.DataFrame), "The function should return a DataFrame"
    assert len(df) > 0, "The DataFrame should not be empty"
    assert set(df.columns) == {'X', 'Y'}, "The DataFrame should have columns 'X' and 'Y'"
    assert df.shape[0] == 1000, "The DataFrame should have 1000 rows"
    assert df.shape[1] == 2, "The DataFrame should have 2 columns"