import string

import pandas as pd
from src_1031 import task_func


def test_task_func():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 26**3
    assert all(df.columns == ["Letter 1", "Letter 2", "Letter 3"])
    assert all(df["Letter 1"].isin(string.ascii_lowercase))
    assert all(df["Letter 2"].isin(string.ascii_lowercase))
    assert all(df["Letter 3"].isin(string.ascii_lowercase))