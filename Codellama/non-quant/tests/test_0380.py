import pandas as pd
from src_0380 import task_func


def test_task_func():
    length = 10
    df = task_func(length)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (length, len(COLUMNS))
    assert all(df.columns == COLUMNS)
    assert all(df.dtypes == np.int64)
    assert all(df.values >= 0)
    assert all(df.values <= 100)