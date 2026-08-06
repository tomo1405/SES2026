import pytest
from src_0630 import task_func
import os
import pandas as pd

# Mocking os.path.exists and os.makedirs to prevent actual directory creation
class MockOsModule:
    def __init__(self):
        self.exists_calls = []
        self.makedirs_calls = []

    def exists(self, path):
        self.exists_calls.append(path)
        return False  # Simulate that the directory does not exist

    def makedirs(self, path):
        self.makedirs_calls.append(path)

@pytest.fixture
def mock_os(monkeypatch):
    mock_os_module = MockOsModule()
    monkeypatch.setattr(os, 'path', mock_os_module)
    monkeypatch.setattr(os, 'makedirs', mock_os_module.makedirs)
    return mock_os_module

def test_task_func(mock_os, tmpdir):
    # Prepare test data
    dataset = [pd.DataFrame({'A': [1, 2], 'B': [3, 4]}), pd.DataFrame({'C': [5, 6], 'D': [7, 8]})]
    filename = 'test_output.csv'
    output_dir = str(tmpdir)

    # Call the function
    result = task_func(dataset, filename, output_dir)

    # Check if the directory was created
    assert mock_os.makedirs_calls == [output_dir]

    # Check if the file was written correctly
    expected_file_path = os.path.join(output_dir, filename)
    assert os.path.exists(expected_file_path)

    with open(expected_file_path, 'r') as f:
        content = f.read()
        expected_content = (
            "A,B\n"
            "1,3\n"
            "2,4\n"
            "------\n"
            "C,D\n"
            "5,7\n"
            "6,8\n"
        )
        assert content == expected_content

    # Check if the operation completion message is correct
    assert "Operation completed in" in result

def test_task_func_existing_directory(mock_os, tmpdir):
    # Prepare test data
    dataset = [pd.DataFrame({'A': [1, 2], 'B': [3, 4]})]
    filename = 'test_output.csv'
    output_dir = str(tmpdir)

    # Simulate that the directory already exists
    mock_os.exists_calls = [output_dir]

    # Call the function
    result = task_func(dataset, filename, output_dir)

    # Check if the directory was not recreated
    assert mock_os.makedirs_calls == []

    # Check if the file was written correctly
    expected_file_path = os.path.join(output_dir, filename)
    assert os.path.exists(expected_file_path)

    with open(expected_file_path, 'r') as f:
        content = f.read()
        expected_content = (
            "A,B\n"
            "1,3\n"
            "2,4\n"
        )
        assert content == expected_content

    # Check if the operation completion message is correct
    assert "Operation completed in" in result