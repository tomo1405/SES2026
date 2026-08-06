import os
import pandas as pd
import numpy as np
import pytest
from src_0410 import task_func

@pytest.fixture
def excel_file_path():
    return 'path/to/excel/file'

@pytest.fixture
def file_name():
    return 'example.xlsx'

@pytest.fixture
def column_name():
    return 'example_column'

def test_file_not_found(monkeypatch, excel_file_path, file_name):
    monkeypatch.setattr(os.path, 'exists', lambda x: False)
    with pytest.raises(FileNotFoundError):
        task_func(excel_file_path, file_name, 'example_column')

def test_column_not_found(monkeypatch, excel_file_path, file_name, column_name):
    df = pd.DataFrame({'other_column': [1, 2, 3]})
    monkeypatch.setattr(pd, 'read_excel', lambda x: df)
    with pytest.raises(ValueError):
        task_func(excel_file_path, file_name, column_name)

def test_valid_input(monkeypatch, excel_file_path, file_name, column_name):
    df = pd.DataFrame({column_name: [1, 2, 3]})
    monkeypatch.setattr(pd, 'read_excel', lambda x: df)
    monkeypatch.setattr(os.path, 'exists', lambda x: True)
    result = task_func(excel_file_path, file_name, column_name)
    expected_result = {'mean': 2.0, 'median': 2.0, 'std_dev': 1.0}
    assert result == expected_result