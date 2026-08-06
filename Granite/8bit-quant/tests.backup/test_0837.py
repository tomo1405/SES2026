import os
import shutil
import csv
import pytest

from src_0837 import task_func

def test_task_func():
    # Test case 1: target_value is found in the first row of a CSV file
    csv_file_content = [
        ['332', 'example1', 'value1'],
        ['444', 'example2', 'value2'],
        ['555', 'example3', 'value3']
    ]
    with open('test_file.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(csv_file_content)
    result = task_func(target_value='332', csv_dir='.', processed_dir='.', simulate=False)
    assert result == {'test_file.csv': 0}
    os.remove('test_file.csv')

    # Test case 2: target_value is not found in any CSV file
    csv_file_content = [
        ['444', 'example1', 'value1'],
        ['555', 'example2', 'value2'],
        ['666', 'example3', 'value3']
    ]
    with open('test_file.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(csv_file_content)
    result = task_func(target_value='332', csv_dir='.', processed_dir='.', simulate=False)
    assert result == {}
    os.remove('test_file.csv')

    # Test case 3: target_value is found in the last row of a CSV file
    csv_file_content = [
        ['332', 'example1', 'value1'],
        ['444', 'example2', 'value2'],
        ['332', 'example3', 'value3']
    ]
    with open('test_file.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(csv_file_content)
    result = task_func(target_value='332', csv_dir='.', processed_dir='.', simulate=False)
    assert result == {'test_file.csv': 2}
    os.remove('test_file.csv')