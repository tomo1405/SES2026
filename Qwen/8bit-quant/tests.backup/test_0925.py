import pytest
from src_0925 import task_func
import pandas as pd
import os
import sys

# Mocking the os.path.exists function
class TestTaskFunc:
    def test_file_not_exists(self, monkeypatch):
        mock_exists = monkeypatch.setattr(os.path, 'exists', lambda x: False)
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            task_func('non_existent_file.csv', 'some_column')
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == 1

    def test_column_exists(self, monkeypatch):
        # Create a mock DataFrame
        data = {'some_column': ['value1\nvalue2', 'value3']}
        df = pd.DataFrame(data)

        # Mock the read_csv function to return our mock DataFrame
        monkeypatch.setattr(pd, 'read_csv', lambda x: df)

        # Call the function
        result_df = task_func('some_file.csv', 'some_column')

        # Check if the newline characters have been replaced
        assert result_df['some_column'].tolist() == ['value1<br>value2', 'value3']

    def test_column_does_not_exist(self, monkeypatch, capsys):
        # Create a mock DataFrame
        data = {'another_column': ['value1', 'value2']}
        df = pd.DataFrame(data)

        # Mock the read_csv function to return our mock DataFrame
        monkeypatch.setattr(pd, 'read_csv', lambda x: df)

        # Call the function
        result_df = task_func('some_file.csv', 'some_column')

        # Check if the column was not modified
        assert result_df.equals(df)

        # Capture and check the printed output
        captured = capsys.readouterr()
        assert "Column 'some_column' does not exist in the DataFrame. No changes were made." in captured.out