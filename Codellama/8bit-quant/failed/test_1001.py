import pytest
from src_1001 import task_func

def test_task_func():
    url = "https://example.com/data.json"
    df = task_func(url)
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] > 0
    assert df.shape[1] > 0
    assert all(df.columns == ["column1", "column2", "column3"])