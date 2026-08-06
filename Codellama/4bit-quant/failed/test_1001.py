import pytest
from src_1001 import task_func

def test_task_func():
    url = "https://www.example.com/data.json"
    df = task_func(url)
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] > 0
    assert df.shape[1] > 0