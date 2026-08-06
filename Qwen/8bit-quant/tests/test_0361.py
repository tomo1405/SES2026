import pytest
from src_0361 import task_func
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

# Mocking the file system to simulate file existence
class MockFileExists:
    def __init__(self, exists=True):
        self.exists = exists

    def __call__(self, path):
        return self.exists

# Mocking the Excel file reading
class MockExcelReader:
    def __init__(self, data):
        self.data = data

    def read_excel(self, file_location, sheet_name):
        return pd.DataFrame(self.data)

@pytest.fixture
def mock_file_exists(monkeypatch):
    monkeypatch.setattr(os.path, 'exists', MockFileExists())

@pytest.fixture
def mock_excel_reader(monkeypatch):
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    monkeypatch.setattr(pd, 'read_excel', MockExcelReader(data).read_excel)

def test_task_func(mock_file_exists, mock_excel_reader):
    file_location = "test.xlsx"
    sheet_name = "Sheet1"
    result, fig = task_func(file_location, sheet_name)

    # Check if the result dictionary is correct
    expected_result = {
        'A': {'mean': 2.0, 'std': 0.816496580927726},
        'B': {'mean': 5.0, 'std': 0.816496580927726}
    }
    assert result == expected_result

    # Check if the figure is created
    assert isinstance(fig, plt.Figure)

def test_task_func_file_not_found(mock_file_exists, monkeypatch):
    file_location = "non_existent_file.xlsx"
    sheet_name = "Sheet1"
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(file_location, sheet_name)
    assert str(excinfo.value) == f"No file found at {file_location}"

def test_task_func_invalid_sheet_name(mock_file_exists, mock_excel_reader, monkeypatch):
    file_location = "test.xlsx"
    sheet_name = "NonExistentSheet"
    with pytest.raises(ValueError) as excinfo:
        task_func(file_location, sheet_name)
    assert "Error reading sheet:" in str(excinfo.value)