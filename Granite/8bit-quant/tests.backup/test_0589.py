import pytest
from src_0589 import task_func

def test_task_func():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert 'X' in df.columns and 'Y' in df.columns
    assert df.shape == (SIZE, 2)