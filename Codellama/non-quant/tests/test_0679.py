import pytest
from src_0679 import task_func
import pandas as pd
import json
import os
import shutil


def test_task_func_returns_dataframe():
    path = 'path/to/data'
    df = task_func(path)
    assert isinstance(df, pd.DataFrame)


def test_task_func_processes_json_files():
    path = 'path/to/data'
    df = task_func(path)
    assert len(df) > 0


def test_task_func_moves_processed_files():
    path = 'path/to/data'
    processed_path = os.path.join(path, 'processed')
    task_func(path)
    assert os.path.exists(processed_path)
    assert len(os.listdir(processed_path)) > 0


def test_task_func_handles_scalar_values():
    path = 'path/to/data'
    df = task_func(path)
    assert len(df) > 0
    assert df['source'].nunique() > 0