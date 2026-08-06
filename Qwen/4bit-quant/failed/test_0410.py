import pytest
from src_0410 import task_func
import pandas as pd
import numpy as np

# Mocking the os and pandas modules to simulate file existence and data reading
class MockOs:
    def path(self):
        pass

    def join(self, *args):
        return '/'.join(args)

    def exists(self, path):
        return path in self.files

class MockPd:
    def read_excel(self, file_path):
        if file_path in self.data:
            return pd.DataFrame(self.data[file_path])
        else:
            raise FileNotFoundError(f"No file found at {file_path}")

# Setup mock objects
mock_os = MockOs()
mock_pd = MockPd()

# Define test cases
@pytest.fixture
def setup_data():
    mock_os.files = {
        '/path/to/file.xlsx': True,
        '/path/to/missing_file.xlsx': False
    }
    mock_pd.data = {
        '/path/to/file.xlsx': {
            'A': [1, 2, 3, 4, 5],
            'B': [5, 4, 3, 2, 1]
        }
    }
    return mock_os, mock_pd

def test_task_func_valid_file_and_column(setup_data):
    mock_os, mock_pd = setup_data
    result = task_func('/path/to', 'file.xlsx', 'A')
    assert result['mean'] == np.mean([1, 2, 3, 4, 5])
    assert result['median'] == np.median([1, 2, 3, 4, 5])
    assert result['std_dev'] == np.std([1, 2, 3, 4, 5])

def test_task_func_missing_file(setup_data):
    mock_os, mock_pd = setup_data
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func('/path/to', 'missing_file.xlsx', 'A')
    assert str(excinfo.value) == "No file found at /path/to/missing_file.xlsx"

def test_task_func_missing_column(setup_data):
    mock_os, mock_pd = setup_data
    with pytest.raises(ValueError) as excinfo:
        task_func('/path/to', 'file.xlsx', 'C')
    assert str(excinfo.value) == "Column 'C' not found in the Excel file."