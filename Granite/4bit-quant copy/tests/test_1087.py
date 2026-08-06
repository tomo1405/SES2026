import string
import random
import pandas as pd
import numpy as np
from src_1087 import task_func

NUM_SAMPLES = 1000  # Number of samples

def test_task_func():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == NUM_SAMPLES
    assert "String Field" in df.columns
    assert "Float Field" in df.columns
    for row in df.itertuples():
        assert isinstance(row.String_Field, str)
        assert isinstance(row.Float_Field, str)

def test_task_func_string_field():
    df = task_func()
    for row in df.itertuples():
        assert len(row.String_Field) == 10

def test_task_func_float_field():
    df = task_func()
    for row in df.itertuples():
        assert float(row.Float_Field) >= 0 and float(row.Float_Field) <= 10000