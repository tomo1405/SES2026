import pytest
from src_0073 import task_func
import pandas as pd
import numpy as np
import os

# Mocking os.listdir and pd.read_csv to simulate file operations
class MockOsListDir:
    def __init__(self, files):
        self.files = files

    def listdir(self, directory):
        return self.files

class MockPdReadCsv:
    def __init__(self, data):
        self.data = data

    def read_csv(self, path):
        return pd.DataFrame(self.data)

@pytest.fixture
def mock_os_listdir(monkeypatch):
    def mock_listdir(directory):
        return ['file1.csv', 'file2.csv', 'file3.csv']
    monkeypatch.setattr(os, 'listdir', mock_listdir)

@pytest.fixture
def mock_pd_read_csv(monkeypatch):
    def mock_read_csv(path):
        return pd.DataFrame({
            'email': ['test@example.com'],
            'list': ['[1, 2, 3]']
        })
    monkeypatch.setattr(pd, 'read_csv', mock_read_csv)

def test_task_func_with_files(mock_os_listdir, mock_pd_read_csv):
    directory = '/path/to/directory'
    df, hist = task_func(directory)
    assert isinstance(df, pd.DataFrame)
    assert 'email' in df.columns
    assert 'list' in df.columns
    assert 'sum' in df.columns
    assert 'mean' in df.columns
    assert 'median' in df.columns
    assert df['sum'].iloc[0] == 6
    assert df['mean'].iloc[0] == 2.0
    assert df['median'].iloc[0] == 2.0
    assert hist is not None

def test_task_func_no_csv_files(monkeypatch):
    def mock_listdir(directory):
        return []
    monkeypatch.setattr(os, 'listdir', mock_listdir)

    directory = '/path/to/directory'
    df, hist = task_func(directory)
    assert df.empty
    assert df.columns.tolist() == ['email', 'list', 'sum', 'mean', 'median']
    assert hist is None

def test_task_func_single_csv_file(mock_os_listdir, mock_pd_read_csv):
    directory = '/path/to/directory'
    df, hist = task_func(directory)
    assert isinstance(df, pd.DataFrame)
    assert 'email' in df.columns
    assert 'list' in df.columns
    assert 'sum' in df.columns
    assert 'mean' in df.columns
    assert 'median' in df.columns
    assert df['sum'].iloc[0] == 6
    assert df['mean'].iloc[0] == 2.0
    assert df['median'].iloc[0] == 2.0
    assert hist is not None

def test_task_func_multiple_csv_files(mock_os_listdir, mock_pd_read_csv):
    directory = '/path/to/directory'
    df, hist = task_func(directory)
    assert isinstance(df, pd.DataFrame)
    assert 'email' in df.columns
    assert 'list' in df.columns
    assert 'sum' in df.columns
    assert 'mean' in df.columns
    assert 'median' in df.columns
    assert df['sum'].iloc[0] == 6
    assert df['mean'].iloc[0] == 2.0
    assert df['median'].iloc[0] == 2.0
    assert hist is not None