import numpy as np
import pandas as pd
from src_0387 import task_func

def test_task_func():
    length = 100
    min_value = 0
    max_value = 100
    df = task_func(length, min_value, max_value)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (length, len(COLUMNS))
    for col in COLUMNS:
        assert df[col].isna().sum() == 0
        assert df[col].max() <= max_value
        assert df[col].min() >= min_value