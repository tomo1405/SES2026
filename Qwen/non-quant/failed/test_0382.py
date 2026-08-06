import pytest
from src_0382 import task_func
import pandas as pd
import os
import matplotlib.pyplot as plt

# Mocking os.path.exists to simulate file existence
def mock_exists(path):
    return True

# Mocking pd.read_csv to simulate reading a DataFrame
def mock_read_csv(path):
    data = {
        'Index': [0, 1, 2],
        'Feature1': [1.0, 2.0, 3.0],
        'Feature2': [4.0, 5.0, 6.0]
    }
    return pd.DataFrame(data)

# Mocking plt.subplots and sns.barplot to simulate plotting
def mock_subplots():
    class MockAx:
        def set_title(self, title):
            pass
    return None, MockAx()

@pytest.fixture(autouse=True)
def patch_dependencies(monkeypatch):
    monkeypatch.setattr(os.path, 'exists', mock_exists)
    monkeypatch.setattr(pd, 'read_csv', mock_read_csv)
    monkeypatch.setattr(plt, 'subplots', mock_subplots)

def test_task_func_file_not_found(monkeypatch):
    def mock_exists(path):
        return False
    monkeypatch.setattr(os.path, 'exists', mock_exists)
    
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func('non_existent_file.csv')
    assert str(excinfo.value) == "The file 'non_existent_file.csv' does not exist."

def test_task_func_target_column_not_found():
    data = {
        'Index': [0, 1, 2],
        'Feature1': [1.0, 2.0, 3.0],
        'Feature2': [4.0, 5.0, 6.0]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError) as excinfo:
        task_func(file_path=None, target_column='NonExistentColumn')
    assert str(excinfo.value) == "The specified target column 'NonExistentColumn' does not exist in the CSV file."

def test_task_func_successful_execution():
    ax, importances = task_func(file_path=None, target_column='Index')
    assert isinstance(ax, plt.Axes)
    assert isinstance(importances, list)
    assert len(importances) == 2  # Two features ('Feature1', 'Feature2')