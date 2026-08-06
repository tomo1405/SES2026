python
import csv
import json
import os
import pytest

def task_func(file_name):
    if not os.path.exists(file_name):
        raise FileNotFoundError("File does not exist.")

    data = []

    with open(file_name, 'r') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            data.append(row)

    json_file_name = file_name.split('.')[0] + '.json'

    with open(json_file_name, 'w') as f:
        json.dump(data, f)

    return json_file_name

def test_task_func():
    # Test case 1: Valid input file
    file_name = 'test.csv'
    with open(file_name, 'w') as f:
        f.write('name,age\n')
        f.write('John,30\n')
        f.write('Jane,25\n')
    assert task_func(file_name) == 'test.json'
    os.remove(file_name)
    os.remove('test.json')

    # Test case 2: Invalid input file
    file_name = 'test.csv'
    with open(file_name, 'w') as f:
        f.write('name,age\n')
        f.write('John,30\n')
        f.write('Jane,25\n')
    os.rename(file_name, 'test.txt')
    with pytest.raises(FileNotFoundError):
        task_func('test.txt')
    os.remove('test.txt')