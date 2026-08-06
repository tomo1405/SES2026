import pytest
from src_0882 import task_func
import pandas as pd
import numpy as np

# Mocking the CSV file for testing
@pytest.fixture
def mock_csv_file(tmp_path):
    csv_content = """data
123x
abc
456X
789y"""
    csv_file = tmp_path / "test.csv"
    with open(csv_file, "w") as f:
        f.write(csv_content)
    return csv_file

def test_task_func_default(mock_csv_file):
    result = task_func(mock_csv_file)
    expected_data = ['123x', '456X']
    assert all(item in result['data'].values for item in expected_data)

def test_task_func_with_sample_size(mock_csv_file):
    result = task_func(mock_csv_file, sample_size=1, seed=42)
    assert len(result) == 1
    assert result['data'].iloc[0] in ['123x', '456X']

def test_task_func_no_matches(mock_csv_file):
    result = task_func(mock_csv_file, pattern='z')
    assert result.empty

def test_task_func_invalid_column_name(mock_csv_file):
    with pytest.raises(KeyError):
        task_func(mock_csv_file, column_name='invalid_column')

def test_task_func_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        task_func('nonexistent.csv')