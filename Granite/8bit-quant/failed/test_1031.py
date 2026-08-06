import pytest
from src_1031 import task_func

def test_task_func():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (26*26*26, 3)
    assert df.columns.tolist() == ["Letter 1", "Letter 2", "Letter 3"]
    assert df["Letter 1"].unique().tolist() == list(string.ascii_lowercase)
    assert df["Letter 2"].unique().tolist() == list(string.ascii_lowercase)
    assert df["Letter 3"].unique().tolist() == list(string.ascii_lowercase)