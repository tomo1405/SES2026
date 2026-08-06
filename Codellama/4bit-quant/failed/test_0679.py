import pytest
from src_0679 import task_func
import pandas as pd
import json
import os
import shutil

def test_task_func():
    path = 'path/to/files'
    df = task_func(path)
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] > 0
    assert 'source' in df.columns
    assert all(df['source'] == 'filename')

def test_task_func_with_scalar_data():
    path = 'path/to/files'
    data = {'key': 'value'}
    with open(os.path.join(path, 'scalar.json'), 'w') as file:
        json.dump(data, file)
    df = task_func(path)
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] == 1
    assert 'source' in df.columns
    assert all(df['source'] == 'scalar.json')

def test_task_func_with_multiple_files():
    path = 'path/to/files'
    data = {'key': 'value'}
    for i in range(10):
        with open(os.path.join(path, f'file{i}.json'), 'w') as file:
            json.dump(data, file)
    df = task_func(path)
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] == 10
    assert 'source' in df.columns
    assert all(df['source'] == 'file{i}.json')

def test_task_func_with_invalid_file():
    path = 'path/to/files'
    with open(os.path.join(path, 'invalid.json'), 'w') as file:
        file.write('invalid data')
    df = task_func(path)
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] == 0
    assert 'source' not in df.columns

def test_task_func_with_missing_file():
    path = 'path/to/files'
    df = task_func(path)
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] == 0
    assert 'source' not in df.columns