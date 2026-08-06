import pytest
from src_0595 import task_func
import os
import csv
import shutil
from datetime import datetime

def test_task_func():
    # Define a temporary directory for testing
    temp_dir = './temp_output'
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    # Call the function
    file_path = task_func(3, temp_dir)

    # Check if the file exists
    assert os.path.exists(file_path), "The file does not exist"

    # Read the CSV file
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

    # Check the header
    assert rows[0] == ['Time', 'Condition'], "Header is incorrect"

    # Check the number of rows (including the header)
    assert len(rows) == 4, "Incorrect number of rows"

    # Check the backup directory and file
    backup_path = os.path.join(temp_dir, 'backup/weather_data.csv')
    assert os.path.exists(backup_path), "Backup file does not exist"

    # Clean up the temporary directory
    shutil.rmtree(temp_dir)