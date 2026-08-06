import pytest
from src_0411 import task_func
import pandas as pd
import os

# Mocking os.path.exists to simulate file existence
class MockOsPathExists:
    def __init__(self, exists=True):
        self.exists = exists

    def __call__(self, path):
        return self.exists

# Mocking pd.read_excel to simulate reading an Excel file
class MockPdReadExcel:
    def __init__(self, data):
        self.data = data

    def __call__(self, *args, **kwargs):
        return pd.DataFrame(self.data)

@pytest.fixture
def mock_os_path_exists(monkeypatch):
    monkeypatch.setattr(os.path, 'exists', MockOsPathExists())

@pytest.fixture
def mock_pd_read_excel(monkeypatch):
    def mock_data():
        return {
            'date_column': ['2023-01-01', '2023-01-15', '2023-02-01'],
            'value_column': [10, 20, 30]
        }
    monkeypatch.setattr(pd, 'read_excel', MockPdReadExcel(mock_data()))

def test_task_func_file_not_found(mock_os_path_exists):
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func('/nonexistent/path', 'file.xlsx', 'date_column', '2023-01-01', '2023-01-31')
    assert str(excinfo.value) == "The file /nonexistent/path/file.xlsx does not exist."

def test_task_func_column_not_found(mock_os_path_exists, mock_pd_read_excel):
    with pytest.raises(ValueError) as excinfo:
        task_func('/valid/path', 'file.xlsx', 'nonexistent_column', '2023-01-01', '2023-01-31')
    assert str(excinfo.value) == "Column nonexistent_column does not exist in the DataFrame."

def test_task_func_date_format_error(mock_os_path_exists, mock_pd_read_excel):
    with pytest.raises(ValueError) as excinfo:
        task_func('/valid/path', 'file.xlsx', 'date_column', '01-01-2023', '01-31-2023')
    assert str(excinfo.value) == "Date format is incorrect. Please use 'yyyy-mm-dd' format."

def test_task_func_success(mock_os_path_exists, mock_pd_read_excel):
    result_df = task_func('/valid/path', 'file.xlsx', 'date_column', '2023-01-01', '2023-01-31')
    expected_df = pd.DataFrame({
        'date_column': ['2023-01-01', '2023-01-15'],
        'value_column': [10, 20]
    })
    pd.testing.assert_frame_equal(result_df.reset_index(drop=True), expected_df.reset_index(drop=True))