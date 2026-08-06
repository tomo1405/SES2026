import pytest
from src_0679 import task_func
import pandas as pd
import json
import os
import shutil

def test_task_func():
    path = 'path/to/data'
    df = task_func(path)
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] > 0
    assert df.shape[1] > 0
    assert 'source' in df.columns
    assert all(df['source'] == 'filename')