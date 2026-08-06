import numpy as np
import pandas as pd
from src_0387 import task_func

# Constants
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']

def test_task_func_shape():
    length = 100
    df = task_func(length)
    assert df.shape == (length, len(COLUMNS))

def test_task_func_min_max():
    length = 100
    min_value = 50
    max_value = 150
    df = task_func(length, min_value, max_value)
    assert (df >= min_value).all().all() and (df <= max_value).all().all()

def test_task_func_columns():
    length = 100
    df = task_func(length)
    assert list(df.columns) == COLUMNS