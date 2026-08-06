import pandas as pd
from src_0194 import task_func


def test_task_func():
    rows = 10
    columns = 5
    df = task_func(rows, columns)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == rows
    assert len(df.columns) == columns
    for col in df.columns:
        assert col in data
        assert isinstance(df[col], data[col])