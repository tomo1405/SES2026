import pytest
from src_0361 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Mocking the file system to test file existence
class MockPath:
    def __init__(self, exists=True):
        self.exists_value = exists

    def exists(self, path):
        return self.exists_value

# Mocking the pandas read_excel function
def mock_read_excel(file_location, sheet_name):
    # Create a sample DataFrame
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    return pd.DataFrame(data)

# Mocking the matplotlib plot functions
class MockFigure:
    def __init__(self):
        self.ax = MockAxes()

class MockAxes:
    def bar(self, *args, **kwargs):
        pass

    def set_title(self, title):
        pass

    def set_xlabel(self, label):
        pass

    def set_ylabel(self, label):
        pass

@pytest.fixture
def mock_file_exists(monkeypatch):
    monkeypatch.setattr(os.path, 'exists', lambda x: True)

@pytest.fixture
def mock_file_not_exists(monkeypatch):
    monkeypatch.setattr(os.path, 'exists', lambda x: False)

@pytest.fixture
def mock_pandas_read_excel(monkeypatch):
    monkeypatch.setattr(pd, 'read_excel', mock_read_excel)

@pytest.fixture
def mock_matplotlib_plot(monkeypatch):
    monkeypatch.setattr(plt, 'subplots', lambda: (MockFigure(), MockAxes()))

def test_task_func_file_not_found(mock_file_not_exists):
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func("non_existent_file.xlsx", "Sheet1")
    assert str(excinfo.value) == "No file found at non_existent_file.xlsx"

def test_task_func_invalid_sheet_name(mock_file_exists, mock_pandas_read_excel):
    with pytest.raises(ValueError) as excinfo:
        task_func("valid_file.xlsx", "InvalidSheet")
    assert str(excinfo.value) == "Error reading sheet: Sheet 'InvalidSheet' is not found"

def test_task_func_valid_input(mock_file_exists, mock_pandas_read_excel, mock_matplotlib_plot):
    result, fig = task_func("valid_file.xlsx", "Sheet1")
    expected_result = {
        'A': {'mean': 2.0, 'std': 1.0},
        'B': {'mean': 5.0, 'std': 1.0}
    }
    assert result == expected_result
    assert isinstance(fig, MockFigure)