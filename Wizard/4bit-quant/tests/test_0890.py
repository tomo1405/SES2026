python
import os
import pandas as pd
import numpy as np
import pytest

from src_0890 import task_func

def test_task_func():
    data_dir = "data"
    csv_file = "test.csv"
    df = task_func(data_dir, csv_file)
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] > 0
    assert df.shape[1] > 0
    for column in df.columns:
        assert df[column].isnull().sum() == 0