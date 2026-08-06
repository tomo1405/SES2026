import os
import shutil
import csv
import pytest
from src_0837 import task_func

def test_task_func():
    # Test case 1: target_value is found in the first row of a CSV file
    csv_file_content = [
        ['332', 'Name 1', 'Age 1'],
        ['222', 'Name 2', 'Age 2'],
        ['111', 'Name 3', 'Age 3']
    ]
    with open('test_file.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(csv_file_content)
    result = task_func(target_value='332', csv_dir='.', processed_dir='.', simulate=False)
    assert result == {'test_file.csv': 0}
    os.remove('test_file.csv')

    # Test case 2: target_value is not found in any CSV file
    csv_file_content = [
        ['444', 'Name 1', 'Age 1'],
        ['555', 'Name 2', 'Age 2'],
        ['666', 'Name 3', 'Age 3']
    ]
    with open('test_file.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(csv_file_content)
    result = task_func(target_value='332', csv_dir='.', processed_dir='.', simulate=False)
    assert result == {}
    os.remove('test_file.csv')

    # Test case 3: target_value is found in multiple CSV files
    csv_file_content_1 = [
        ['332', 'Name 1', 'Age 1'],
        ['222', 'Name 2', 'Age 2'],
        ['111', 'Name 3', 'Age 3']
    ]
    with open('test_file_1.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(csv_file_content_1)
    csv_file_content_2 = [
        ['332', 'Name 4', 'Age 4'],
        ['222', 'Name 5', 'Age 5'],
        ['111', 'Name 6', 'Age 6']
    ]
    with open('test_file_2.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(csv_file_content_2)
    result = task_func(target_value='332', csv_dir='.', processed_dir='.', simulate=False)
    assert result == {'test_file_1.csv': 0, 'test_file_2.csv': 0}
    os.remove('test_file_1.csv')
    os.remove('test_file_2.csv')