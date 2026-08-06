import pytest
from src_0068 import task_func
import os
import pandas as pd

# Mocking os and os.path functions for testing
class MockOsModule:
    def __init__(self, files):
        self.files = files

    def listdir(self, dir_path):
        return self.files

    def path(self):
        class MockPath:
            def join(self, *args):
                return '/'.join(args)

            def getsize(self, file_path):
                # Simulate file sizes
                return len(file_path)  # Using length as a mock size

        return MockPath()

@pytest.fixture
def mock_os(monkeypatch):
    files = ['EMPLOYEE1.txt', 'EMPLOYEE2.txt', 'NOTEMPLOYEE.txt']
    monkeypatch.setattr('os', MockOsModule(files))
    return files

def test_task_func(mock_os, tmpdir):
    dir_path = str(tmpdir)
    df = task_func(dir_path)
    
    # Expected DataFrame
    expected_data = {
        'File': ['EMPLOYEE1.txt', 'EMPLOYEE2.txt'],
        'Size': [len(os.path.join(dir_path, 'EMPLOYEE1.txt')), len(os.path.join(dir_path, 'EMPLOYEE2.txt'))]
    }
    expected_df = pd.DataFrame(expected_data)

    # Check if the returned DataFrame matches the expected DataFrame
    pd.testing.assert_frame_equal(df, expected_df)

def test_task_func_no_matching_files(mock_os, tmpdir):
    dir_path = str(tmpdir)
    df = task_func(dir_path, pattern='^NO')

    # Expected DataFrame with no rows
    expected_df = pd.DataFrame(columns=['File', 'Size'])

    # Check if the returned DataFrame matches the expected DataFrame
    pd.testing.assert_frame_equal(df, expected_df)