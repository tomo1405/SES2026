import pandas as pd
from src_1087 import task_func


def test_task_func():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == NUM_SAMPLES
    assert "String Field" in df.columns
    assert "Float Field" in df.columns
    assert all(df["String Field"].str.len() == 10)
    assert all(df["Float Field"].str.len() == 5)
    assert all(df["Float Field"].str.contains("."))
    assert all(df["Float Field"].str.contains(","))