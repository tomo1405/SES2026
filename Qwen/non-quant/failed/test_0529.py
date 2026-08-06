import pytest
from src_0529 import task_func
import pandas as pd
import matplotlib.pyplot as plt

# Mocking the file operations for testing
class MockFile:
    def __init__(self, content):
        self.content = content
        self.closed = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.closed = True

    def read(self):
        return self.content

    def close(self):
        self.closed = True

def mock_open(file_path, mode):
    if file_path == "test.csv":
        return MockFile("col1,col2\nvalue1,value2\nvalue1,value2\nvalue3,value4")
    else:
        raise FileNotFoundError("File not found")

@pytest.fixture(autouse=True)
def patch_open(monkeypatch):
    monkeypatch.setattr('builtins.open', mock_open)

def test_task_func_valid_csv():
    duplicates, ax = task_func("test.csv")
    assert duplicates == {('value1', 'value2'): 2}
    assert isinstance(ax, plt.Axes)

def test_task_func_invalid_file_format():
    with pytest.raises(ValueError) as excinfo:
        task_func("test.txt")
    assert str(excinfo.value) == "Invalid file format. Only .csv files are accepted."

def test_task_func_no_duplicates():
    duplicates, ax = task_func("test_no_duplicates.csv")
    assert duplicates == {}
    assert ax is None

def test_task_func_empty_file():
    duplicates, ax = task_func("empty.csv")
    assert duplicates == {}
    assert ax is None

def test_task_func_single_row():
    duplicates, ax = task_func("single_row.csv")
    assert duplicates == {}
    assert ax is None