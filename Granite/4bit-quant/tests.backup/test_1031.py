import pytest
from src_1031 import task_func

def test_task_func():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (52, 3)
    assert df.columns.tolist() == ["Letter 1", "Letter 2", "Letter 3"]