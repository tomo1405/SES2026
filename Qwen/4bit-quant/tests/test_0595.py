import pytest
from src_0595 import task_func
import os
import csv
import shutil

# Mocking datetime to control the time output in the CSV
from unittest.mock import patch

@pytest.fixture
def setup_output_dir(tmpdir):
    # Create a temporary directory for output
    output_dir = tmpdir.mkdir("output")
    return str(output_dir)

@patch('src_0595.datetime')
def test_task_func(mock_datetime, setup_output_dir):
    # Set up mock datetime to return a fixed value
    mock_datetime.now.return_value.strftime.return_value = '12:34:56.789012'
    
    hours = 3
    file_path = task_func(hours, output_dir=setup_output_dir)
    
    # Check if the file exists
    assert os.path.exists(file_path)
    
    # Read the content of the file
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    
    # Check the header
    assert rows[0] == ['Time', 'Condition']
    
    # Check the number of rows
    assert len(rows) == hours + 1
    
    # Check the content of each row
    for row in rows[1:]:
        assert row[0] == '12:34:56.789012'
        assert row[1] in ['Sunny', 'Cloudy', 'Rainy', 'Snowy', 'Stormy']
    
    # Check if the backup directory and file exist
    backup_path = os.path.join(setup_output_dir, 'backup/weather_data.csv')
    assert os.path.exists(backup_path)
    
    # Clean up
    shutil.rmtree(setup_output_dir)