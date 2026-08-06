import pytest
from src_0647 import task_func
import os
import pandas as pd
from dateutil.parser import parse

# Mocking os.path.isfile to simulate file existence
class MockPath:
    def __init__(self, exists=True):
        self.exists = exists

    def isfile(self, path):
        return self.exists

def test_task_func_file_not_exists(monkeypatch):
    # Mock os.path.isfile to return False
    monkeypatch.setattr(os.path, 'isfile', lambda path: False)
    
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(csv_path='./nonexistent.csv')
    
    assert str(excinfo.value) == "./nonexistent.csv does not exist"

def test_task_func_valid_csv(tmpdir):
    # Create a temporary CSV file
    csv_file = tmpdir.join('data.csv')
    csv_content = """date,value\n2020-01-01,10\n2021-02-02,20\n2022-03-03,30"""
    csv_file.write(csv_content)
    
    # Call the function with the temporary CSV file
    result = task_func(csv_path=str(csv_file))
    
    # Check if the result is a Series with the correct years
    expected_years = pd.Series([2020, 2021, 2022])
    assert all(result.index == expected_years)

def test_task_func_custom_date_column(tmpdir):
    # Create a temporary CSV file with a custom date column
    csv_file = tmpdir.join('data.csv')
    csv_content = """timestamp,value\n2020-01-01,10\n2021-02-02,20\n2022-03-03,30"""
    csv_file.write(csv_content)
    
    # Call the function with the custom date column
    result = task_func(csv_path=str(csv_file), date_column='timestamp')
    
    # Check if the result is a Series with the correct years
    expected_years = pd.Series([2020, 2021, 2022])
    assert all(result.index == expected_years)