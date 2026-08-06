import pytest
from src_0073 import task_func
import pandas as pd
import os
import numpy as np

# Mocking os.listdir and pd.read_csv for testing
class MockedListDir:
    def __init__(self, files):
        self.files = files

    def __call__(self, directory):
        return self.files

class MockedReadCSV:
    def __init__(self, data):
        self.data = data

    def __call__(self, path):
        return pd.DataFrame(self.data)

def test_task_func_no_csv_files(monkeypatch):
    # Arrange
    mock_listdir = MockedListDir([])
    monkeypatch.setattr(os, 'listdir', mock_listdir)
    monkeypatch.setattr(pd, 'read_csv', MockedReadCSV({}))

    # Act
    df, hist = task_func('/path/to/directory')

    # Assert
    expected_df = pd.DataFrame({}, columns=['email', 'list', 'sum', 'mean', 'median'])
    assert df.equals(expected_df)
    assert hist is None

def test_task_func_single_csv_file(monkeypatch):
    # Arrange
    mock_listdir = MockedListDir(['data.csv'])
    mock_data = {
        'email': ['test@example.com'],
        'list': ['[1, 2, 3]']
    }
    monkeypatch.setattr(os, 'listdir', mock_listdir)
    monkeypatch.setattr(pd, 'read_csv', MockedReadCSV(mock_data))

    # Act
    df, hist = task_func('/path/to/directory')

    # Assert
    expected_df = pd.DataFrame({
        'email': ['test@example.com'],
        'list': [[1, 2, 3]],
        'sum': [6],
        'mean': [2.0],
        'median': [2.0]
    })
    assert df.equals(expected_df)
    assert isinstance(hist, np.ndarray)

def test_task_func_multiple_csv_files(monkeypatch):
    # Arrange
    mock_listdir = MockedListDir(['file1.csv', 'file2.csv', 'file3.csv'])
    mock_data = {
        'email': ['test@example.com'],
        'list': ['[1, 2, 3]']
    }
    monkeypatch.setattr(os, 'listdir', mock_listdir)
    monkeypatch.setattr(pd, 'read_csv', MockedReadCSV(mock_data))

    # Act
    df, hist = task_func('/path/to/directory')

    # Assert
    expected_df = pd.DataFrame({
        'email': ['test@example.com'],
        'list': [[1, 2, 3]],
        'sum': [6],
        'mean': [2.0],
        'median': [2.0]
    })
    assert df.equals(expected_df)
    assert isinstance(hist, np.ndarray)

def test_task_func_longest_filename(monkeypatch):
    # Arrange
    mock_listdir = MockedListDir(['short.csv', 'longerfilename.csv', 'longestfilename.csv'])
    mock_data = {
        'email': ['test@example.com'],
        'list': ['[1, 2, 3]']
    }
    monkeypatch.setattr(os, 'listdir', mock_listdir)
    monkeypatch.setattr(pd, 'read_csv', MockedReadCSV(mock_data))

    # Act
    df, hist = task_func('/path/to/directory')

    # Assert
    expected_df = pd.DataFrame({
        'email': ['test@example.com'],
        'list': [[1, 2, 3]],
        'sum': [6],
        'mean': [2.0],
        'median': [2.0]
    })
    assert df.equals(expected_df)
    assert isinstance(hist, np.ndarray)