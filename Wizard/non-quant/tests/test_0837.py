python
import os
import shutil
import csv
import pytest

def task_func(target_value='332', csv_dir='./csv_files/', processed_dir='./processed_files/', simulate=False):
    result = {}

    # Scan the CSV files in the directory
    for filename in os.listdir(csv_dir):
        if filename.endswith('.csv'):
            with open(os.path.join(csv_dir, filename), 'r') as f:
                reader = csv.reader(f)
                for i, row in enumerate(reader):
                    if row[0] == target_value:
                        result[filename] = i
                        break

            # Move the file to the processed directory if not simulating
            if not simulate:
                shutil.move(os.path.join(csv_dir, filename), processed_dir)
    
    return result

def test_task_func():
    # Test case 1: target value is found in the first row of the first CSV file
    assert task_func(target_value='332', csv_dir='./tests/csv_files/', processed_dir='./tests/processed_files/') == {'test1.csv': 0}

    # Test case 2: target value is found in the third row of the second CSV file
    assert task_func(target_value='332', csv_dir='./tests/csv_files/', processed_dir='./tests/processed_files/') == {'test2.csv': 2}

    # Test case 3: target value is not found in any CSV file
    assert task_func(target_value='999', csv_dir='./tests/csv_files/', processed_dir='./tests/processed_files/') == {}

    # Test case 4: simulate flag is set to True, so no files should be moved
    assert task_func(target_value='332', csv_dir='./tests/csv_files/', processed_dir='./tests/processed_files/', simulate=True) == {'test1.csv': 0, 'test2.csv': 2}