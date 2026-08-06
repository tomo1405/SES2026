import pytest
from src_0802 import task_func
import numpy as np

# Mocking the np.genfromtxt function to simulate file reading
@pytest.fixture
def mock_genfromtxt(monkeypatch):
    def mock_function(*args, **kwargs):
        # Simulate different scenarios based on the file name
        if kwargs['file_name'] == 'empty_file.csv':
            return np.array([], dtype=[('col1', int), ('col2', float)])
        elif kwargs['file_name'] == 'single_row_file.csv':
            return np.array([(1, 2.5)], dtype=[('col1', int), ('col2', float)])
        elif kwargs['file_name'] == 'multiple_rows_file.csv':
            return np.array([(1, 2.5), (1, 3.5), (2, 2.5), (2, 2.5)], dtype=[('col1', int), ('col2', float)])
        elif kwargs['file_name'] == 'tied_values_file.csv':
            return np.array([(1, 2.5), (1, 2.5), (2, 3.5), (2, 3.5)], dtype=[('col1', int), ('col2', float)])
        else:
            raise ValueError("Unknown file name")

    monkeypatch.setattr(np, 'genfromtxt', mock_function)

def test_empty_file(mock_genfromtxt):
    result = task_func('empty_file.csv')
    assert result == {}

def test_single_row_file(mock_genfromtxt):
    result = task_func('single_row_file.csv')
    assert result == {'col1': 1, 'col2': 2.5}

def test_multiple_rows_file(mock_genfromtxt):
    result = task_func('multiple_rows_file.csv')
    assert result == {'col1': 1, 'col2': 2.5}

def test_tied_values_file(mock_genfromtxt):
    result = task_func('tied_values_file.csv')
    assert result == {'col1': 1, 'col2': 2.5}