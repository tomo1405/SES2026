import pytest
from src_0890 import task_func
import pandas as pd
import numpy as np
import os

# Mocking the os module to simulate file operations
class MockOsModule:
    def path(self):
        return self

    def join(self, *args):
        return '/'.join(args)

# Mocking the pandas module to simulate DataFrame operations
class MockPandasModule:
    class DataFrame:
        def __init__(self, data=None):
            self.data = data if data is not None else {}

        def __eq__(self, other):
            return self.data == other.data

        def fillna(self, value, inplace=True):
            if inplace:
                for col in self.data:
                    if np.issubdtype(np.array(self.data[col]).dtype, np.number):
                        self.data[col] = [value if pd.isnull(x) else x for x in self.data[col]]
            return self

    @staticmethod
    def read_csv(file_path):
        if file_path == '/data/dummy.csv':
            return MockPandasModule.DataFrame({'A': [1, 2, np.nan], 'B': [4, np.nan, 6]})
        elif file_path == '/data/empty.csv':
            raise pd.errors.EmptyDataError("No data")
        else:
            raise FileNotFoundError("File not found")

# Patching the modules
@pytest.fixture(autouse=True)
def patch_modules(monkeypatch):
    monkeypatch.setattr('src_0890.os', MockOsModule())
    monkeypatch.setattr('src_0890.pd', MockPandasModule())
    monkeypatch.setattr('src_0890.np', np)

def test_task_func_with_valid_data():
    result = task_func('/data', 'dummy.csv')
    expected_df = pd.DataFrame({'A': [1, 2, 2], 'B': [4, 5, 6]})
    assert result == expected_df

def test_task_func_with_empty_data():
    result = task_func('/data', 'empty.csv')
    expected_df = pd.DataFrame()
    assert result == expected_df

def test_task_func_with_nonexistent_file():
    with pytest.raises(FileNotFoundError, match="File not found"):
        task_func('/data', 'nonexistent.csv')